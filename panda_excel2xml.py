from pandas import read_excel
import xml.etree.cElementTree as ET
import lxml.etree as etree

def add_xml(partner_info):
  Partner = ET.SubElement(Partners, "Partner")
  for key, value in partner_info.items():
    ET.SubElement(Partner, key).text = value

def render_xml(Processdata, xml_file):
  tree = ET.ElementTree(Processdata)
  tree.write(xml_file)

  x = etree.parse(xml_file)
  print("\n")
  print(etree.tostring(x, pretty_print=True, encoding="unicode"))

def import_excel(df):
  excel_data = df.to_dict()
  total_rows = len(df.index)
  fields = list(excel_data.keys())

  for i in range(total_rows):
    partner_info = {}
    for field in fields:
      # print(field, excel_data[field][i])
      partner_info[field] = excel_data[field][i]
    
    add_xml(partner_info)

if __name__ == '__main__':
  df = read_excel(r'C:\python_files\import_me.xlsx')

  xml_file = "import_me.xml"
  Processdata = ET.Element("Processdata")
  Partners = ET.SubElement(Processdata, "Partners")

  import_excel(df)
  render_xml(Processdata, xml_file)