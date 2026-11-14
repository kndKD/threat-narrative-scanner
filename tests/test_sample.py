"""Day 1 tests: the sample Nmap XML parses, and its open ports are the
ones the Day 2 parser and Day 4 risk rules will be tested against.
Uses only the standard library — no nmap install needed in CI.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

SAMPLE = Path(__file__).resolve().parents[1] / "data" / "sample_nmap.xml"


def _open_ports():
    tree = ET.parse(SAMPLE)
    ports = []
    for port in tree.getroot().findall(".//port"):
        state = port.find("state").get("state")
        if state == "open":
            service = port.find("service")
            name = service.get("name") if service is not None else ""
            product = service.get("product", "") if service is not None else ""
            ports.append(
                {"port": int(port.get("portid")), "service": name, "product": product}
            )
    return ports


def test_sample_xml_parses():
    tree = ET.parse(SAMPLE)
    assert tree.getroot().tag == "nmaprun"


def test_sample_has_four_open_ports():
    ports = _open_ports()
    assert sorted(p["port"] for p in ports) == [22, 80, 5000, 5432]


def test_sample_postgres_is_the_critical_example():
    ports = {p["port"]: p for p in _open_ports()}
    assert ports[5432]["service"] == "postgresql"
    assert ports[5000]["service"] == "http"
    assert ports[5000]["product"] == "Werkzeug"
