#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import io
# from io import BytesIO

def python_test():
    print "Hello Python!!!"
    pass


def open_xml(file_name):
    "Open xml file"
    tree = ET.parse(file_name)
    root = tree.getroot()
    print root
    return root
    
def new(file_name):
    "Create new xml file"
    xml_file = open(file_name, 'w')
    # root = ET.Element(file)
    return xml_file    


def prettify(elem):
    "Return a pretty-printed XML string for the Element."
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_and_save_xml(file, elem):
    xml_file = new(file)
    if isinstance(elem, basestring):
        xml_file.write(elem)
    else:
        xml_file.write(prettify(elem))
    xml_file.close()


def test_writing():
    top = ET.Element('top')

    comment = ET.Comment('Generated for PyMOTW')
    top.append(comment)

    child = ET.SubElement(top, 'child')
    child.text = 'This child contains text.'

    child_with_tail = ET.SubElement(top, 'child_with_tail')
    child_with_tail.text = 'This child has regular text.'
    child_with_tail.tail = 'And tail text.'

    child_with_entity_ref = ET.SubElement(top, 'child_with_entity_ref')
    child_with_entity_ref.text = 'This outside'

    child_with_entity_ref2 = ET.SubElement(child_with_tail, 'child_of_subchild')
    child_with_entity_ref2.text = 'This inside'

    child_with_entity_ref3 = ET.SubElement(child_with_entity_ref2, 'child_of_sub_sub')
    child_with_entity_ref3.text = 'This inside recursively'

    print prettify(top)

def add_element(parent, text, attributes, text_body):
    new_child = ET.SubElement(parent, text,attributes)
    new_child.text = text_body
    return new_child

def get_root(name):
    return ET.Element(name)

def append_element(root, element):
    root.append(element)

def append_and_save_xml(file, element):
    xml_file = open(file, 'a')
    root = ET.Element(xml_file)
    append_element(root, element)
    print root
    xml_file.close()

def create_element(file, node_parent, node_children ):
    "Create new element in xml file"
    doc = ET.Element(file)
    node = ET.SubElement(doc, node_parent)
    node_child = ET.SubElement(node, node_children)
    # file.insert(2, e)

    et = ET.ElementTree(doc)
    # f = BytesIO()
    # f = ET.tostring(et, encoding='UTF-8', xml_declaration=True)
    f = ET.tostring(et, encoding='UTF-8')
    reparsed = minidom.parseString(f)
    print(reparsed.getvalue())

def create_attributes(file, node, attribute):
    "Add attributes to node"
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


# xmlReporter.AddMessage("EXPECT_HMIRESPONSE", {["Id"] = tostring(id),["Type"] = "AVALIABLE_RESULT"},data)
def write_xml(file, content):
    ""
    ET.tree.write(file)
    pass


# Might be unused
def unused_functions():

    def node_attributes(node):
        "Get node attributes"
        print node.attrib
        return node.attrib
        pass

    # Functions for get information about elements
    def node_children():
        pass


    def node_parent():
        pass


    def doc_xpath():
        "Return path to document"
        pass

    def node_xpath():
        "path to all structure"
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
