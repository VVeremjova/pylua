#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import xml_loader

import xml.etree.ElementTree as ET

# test part
xml_file = "test_report2.xml"
root = xml_loader.get_root('top')

newtext = "some new text"
new_el = xml_loader.add_element(root, "top_child", {'type' :'request', 'size':'44'},"")

xml_loader.add_element(new_el, "param", {'type' :'new_param', 'size':'777'}, "newtext")
# print root
print xml_loader.prettify(root)

result = xml_loader.prettify(root)


xml_loader.create_and_save_xml(xml_file, result)

el2 = xml_loader.add_element(new_el, "param", {'type' :'new_param444', 'size':'234'}, "newtext")

elem = ET.Element("param", {'type' :'new_param55555', 'size':'2356784'})
elem.text = "text"
xml_loader.append_element(root, elem)


xml_loader.create_and_save_xml(xml_file, root)

# xml_loader.append_and_save_xml(xml_file, elem)