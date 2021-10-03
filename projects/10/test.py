import xml.etree.ElementTree as ET

root = ET.Element("root")
sub = ET.SubElement(root, "sub")
sub = ET.SubElement(root, "sub")
sub = ET.SubElement(root, "sub")
sub = ET.SubElement(root, "sub")

tree = ET.ElementTree(root)
with open("test.xml", "wb") as f:
    tree.write(f)