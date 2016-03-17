from xml.dom import minidom

doc = minidom.parse("items.xml")
titles = doc.getElementsByTagName("title")
print len(titles)


