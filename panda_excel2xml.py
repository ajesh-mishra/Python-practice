from pandas import read_excel
from datetime import datetime
import xml.etree.cElementTree as ET
import lxml.etree as etree
from datetime import datetime

class Xml():

  def __init__(self):
    self.timestamp = datetime.now().strftime("%d%b%Y_%H%M%S_%f")
    self.xml_file = "import_me_" + self.timestamp + ".xml"
    self.processdata = ET.Element("Processdata")
    self.partners = ET.SubElement(self.processdata, "Partners")

  def add_xml(self, partner_info):
    self.partner = ET.SubElement(self.partners, "Partner")
    for key, value in partner_info.items():
      ET.SubElement(self.partner, key).text = value

  def render_xml(self):
    tree = ET.ElementTree(self.processdata)
    tree.write(self.xml_file)

    x = etree.parse(self.xml_file)
    return etree.tostring(x, pretty_print=True, encoding="unicode")


def import_excel(df):
  xml = Xml()
  excel_data = df.to_dict()
  total_rows = len(df.index)
  fields = list(excel_data.keys())

  for i in range(total_rows):
    partner_info = {}
    for field in fields:
      partner_info[field] = excel_data[field][i]
    
    xml.add_xml(partner_info)

  return xml.render_xml()


if __name__ == '__main__':

  df = read_excel(r'import_me.xlsx')
  print(import_excel(df))






















