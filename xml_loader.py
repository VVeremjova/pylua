#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def python_test():
    print "Hello Python!!!"
    pass


def open(file_name):
    "Open xml file"
    tree = ET.parse(file_name)
    root = tree.getroot()
    print root
    return root
    pass

def get_attribute_structure(structure, attribute_tag):
    "Return array of attributes in given structure"
    _return_structure = []
    # print structure
    # print attribute_tag
    for structure_body in structure:
        param_name = structure_body.tag
        # print param_name
        if param_name == attribute_tag:
            _params = structure_body.attrib
            # print '|--|-->', param_name, ' -- ',_params
            _return_structure.append(structure_body)
    return _return_structure


def get_attribute_name(structure, attribute):
    "Return value of attribute"
    return structure.get(attribute)


def get_count(structure):
    "Return count of elements in structure"
    return len(structure)

def doc_xpath():
    "Return path to document"
    pass

def node_xpath():
    "path to all structure"
    pass



# Functions for get information about elements
def node_children():
    pass




# Might be unused
def unused_functions():

    def node_attributes(node):
        "Get node attributes"
        print node.attrib
        return node.attrib
        pass


    def node_parent():
        pass


    def new():
        "Create new xml file"
        pass

    def write():
        "Add new eliment to xml"
        pass

    def node_text():
        pass

    def node_name():
        pass

    def node_attr():
        "get attribute"
        pass



    def node_attributes(node):
        "Get node attributes"
        print node.attrib
        return node.attrib
        pass

    def node_eq():
        pass

    def luaopen_xml():
        pass


    def rootNode(root):
        "Retun smthg"
        print root.tag
        return root.tag
        pass

    def doc_createRootNode():
        pass

    def node_addChild():
        pass


    def node_remove():
        pass
    pass



# # test part
# xml_file = "HMI_API.xml"
# root = open(xml_file)

# print "root is:" 
# print root

# elems_in_xml = get_attribute_structure(root, 'interface')
# for elem_in_xml in elems_in_xml: # root.iter('interface'):
#     elems_in_interface = get_attribute_structure(elem_in_xml, 'function')
#     for elem_in_interface in elems_in_interface:
#         print 'elem: ', elem_in_interface
#         get_attribute_structure(elem_in_interface, 'param')
