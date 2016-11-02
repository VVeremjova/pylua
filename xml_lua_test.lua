package.loadlib("libpython2.7.so", "*")
require('lua-python')

python.execute("import xml_loader")

pg = python.globals()

xml_loader = pg.xml_loader
root = python.asattr(xml_loader.open("HMI_API.xml"))

elems_in_xml = python.asindx(python.asattr(xml_loader.get_attribute_structure(root, 'interface')))

count = xml_loader.get_count(elems_in_xml)
print(count)
for i =0, count-1 do 

  print(elems_in_xml[i])
  elems_in_interface = python.asindx(python.asattr(
                        xml_loader.get_attribute_structure
                        (elems_in_xml[i], 'function')))


end



-- in elems_in_xml
    -- elems_in_interface = xml_loader.get_attribute_structure(elem_in_xml, 'function')
--     for elem_in_interface =1,  #elems_in_interface do
--         print ('elem: ')
--         print(elem_in_interface)
--         xml_loader.get_attribute_structure(elem_in_interface, 'param')

--     end

