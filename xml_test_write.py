#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import xml_loader

import xml.etree.ElementTree as ET



xml_loader.python_test()

# xml_loader.path(elem)


# test part
#not work yet
# xml_file = "test_report.xml"
# root = xml_loader.new(xml_file)

# this works
root = ET.Element('top')

# xml_loader.create_element(xml_file, "node_parent", "node_children" )
# xml_loader.test_writing()
newtext = "some new text"
xml_loader.add_element(root, "top_child", {'type' :'request'}, newtext)
# print root
print xml_loader.prettify(root)