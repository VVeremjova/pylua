package.loadlib("libpython2.7.so", "*")
require('lua-python')

python.execute("import xml_loader")

pg = python.globals()

-- print('Hello from Lua!')

xml_loader = pg.xml_loader
-- s = xml_loader.python_test()

root = python.asattr(xml_loader.open("HMI_API.xml"))
-- print(root)
elems_in_xml = python.asattr(xml_loader.get_attribute_structure(root, 'interface'))
print (elems_in_xml)
-- for elem_in_xml = 1, #elems_in_xml do
-- -- for elem_in_xml in elems_in_xml
--     elems_in_interface = xml_loader.get_attribute_structure(elem_in_xml, 'function')
--     for elem_in_interface =1,  #elems_in_interface do
--         print ('elem: ')
--         print(elem_in_interface)
--         xml_loader.get_attribute_structure(elem_in_interface, 'param')

--     end
-- end
