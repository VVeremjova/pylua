#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import xml_loader


xml_loader.python_test()

xml_file = "HMI_API.xml"
elem = xml_loader.open(xml_file)

# xml_loader.path(elem)


# test part
xml_file = "HMI_API.xml"
root = xml_loader.open(xml_file)

print "root is:" 
print root

# for elem_in_xml in root: # root.iter('interface'):
#     interface_attr = elem_in_xml.attrib
#     name = interface_attr["name"]
#     print name
elems_in_xml = xml_loader.get_attribute_structure(root, 'interface')
for elem_in_xml in elems_in_xml: # root.iter('interface'):
    print ('### ',xml_loader.get_attribute_name(elem_in_xml, 'name'))
    elems_in_interface = xml_loader.get_attribute_structure(elem_in_xml, 'function')
    for elem_in_interface in  elem_in_xml:
        # print ' |-->', elem_in_interface 
        if elem_in_interface.tag == 'function':
            functions_name = elem_in_interface.attrib
            print '|-->',functions_name
            function_name = functions_name["name"] 

    # print 'elem: ', elems_in_interface

    for elem_in_interface in elems_in_interface:
        print 'elem: ', elem_in_interface
        xml_loader.get_attribute_structure(elem_in_interface, 'param')
        for function_body in elem_in_interface:
            
            param_name = function_body.tag
            if param_name == 'param':
                _params = function_body.attrib
                print '|--|-->', param_name, ' -- ',_params
            # print function_body