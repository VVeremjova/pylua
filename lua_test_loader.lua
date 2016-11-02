package.loadlib("libpython2.7.so", "*")
require('lua-python')

python.execute("import xml_loader")

local pg = python.globals()


local xml_loader = pg.xml_loader


local module = { }

-- Include result codes that are elements in functions from Mobile Api.
-- Each function with paremeter resultCode that has type Result
-- should contain types of Resultcode directly in function.
-- Other resultCodes are kept in structs  
local function LoadResultCodes( param )
  local resultCodes ={}
  local i = 1
  for _, item in ipairs(param:children("element")) do
     local name = item:attr("name")
     resultCodes[i]=name
     i=i + 1
    end
  return resultCodes
end


local escape_lua_pattern
do
  local matches =
  {
    ["'"] = "%'";
    ["#"] = "";
    ["&"] = "";
  }

  escape_lua_pattern = function(s)
    return (s:gsub(".", matches))
  end
end

local function dump(o)
  if type(o) == 'table' then
    local s = '{ '
    for k,v in pairs(o) do
      if type(k) ~= 'number' then k = '\''..k..'\'' end
      s = s .. '['..k..'] = \'' .. dump(v) .. '\','
    end
    return s .. '}'
  elseif string.match(tostring(o),'[%Wxyz]') then
    return escape_lua_pattern(tostring(o))
  end
  return tostring(o)
end


--Load parameteres in function. Load ResultCodes if 
--type of parameter is "Result"
local function LoadParamsInFunction(param, interface)
  local name = param:attr("name")
  print(name)
  local p_type = param:attr("type")
  local mandatory = param:attr("mandatory")
  local array = param:attr("array")

  if mandatory == nil then 
    mandatory = true
  end

  if array == nil then 
    array = false
  end

  local result_codes = nil
  if name == "resultCode" and p_type == "Result" then 
    result_codes  = LoadResultCodes(param) 
  end

  local data = {}
  data["type"]=p_type
  data["mandatory"]= mandatory
  data["array"] = array
  data["minlength"] = tonumber(param:attr("minlength"))
  data["maxlength"] = tonumber(param:attr("maxlength"))
  data["minsize"] = tonumber(param:attr("minsize"))
  data["maxsize"] = tonumber(param:attr("maxsize"))
  data["minvalue"] = tonumber(param:attr("minvalue"))
  data["maxvalue"] = tonumber(param:attr("maxvalue"))
  data["resultCodes"] = result_codes
  return name, data
end



local function LoadEnums(root, dest)
  local k = 0
  for first, v in pairs (dest.interface) do

    local enums = python.asindx(python.asattr
                      (xml_loader.get_attribute_structure
                        (root[k], 'enum')))
    local count = xml_loader.get_count(enums)
    -- print ("count of enums".. tostring(count))
    if count >0 then
      for i =0, count-1 do 
        local name  = xml_loader.get_attribute_name(enums[i], 'name')
        -- print(name)
        dest.interface[first].enum[name]={}
        local j= 1
        local enum_values = python.asindx(python.asattr
                        (xml_loader.get_attribute_structure
                          (enums[i], 'element')))
        local count_el = xml_loader.get_count(enum_values)
        -- print ("\tcount in enum is:".. tostring(count_el))
        for jk = 0, count_el-1 do
          local enum_value  = xml_loader.get_attribute_name(enum_values[jk], 'name')
          dest.interface[first].enum[name][enum_value]=j
          j= j + 1
        end

      end
    end
    k=k+1
  end
 end
 
  local function LoadStructs(root, dest)
    local k = 0
    for first, v in pairs (dest.interface) do
      local structs = python.asindx(python.asattr
                      (xml_loader.get_attribute_structure
                        (root[k], 'struct')))
      local count = xml_loader.get_count(structs)
      if count >0 then
        for i =0, count-1 do 
          local name  = xml_loader.get_attribute_name(structs[i], 'name')
          local temp_param = {}
          local temp_func = {}
          temp_func["name"] = name

          local param_values = python.asindx(python.asattr
                        (xml_loader.get_attribute_structure
                          (structs[i], 'param')))
          local count_params = xml_loader.get_count(param_values)
          print(count_params)
          for k_it = 0, count_params-1 do
            param_name, param_data = LoadParamsInFunction(param_values[k_it], first)
          end

          dest.interface[first].struct[name]=temp_func
        end
      end

    -- for _, s in ipairs(v.body:children("struct")) do
    --   local name = s:attr("name")
    --   local temp_param = {}
    --   local temp_func = {}
    --   temp_func["name"] = name
    --   for _, item in ipairs(s:children("param")) do
    --     param_name, param_data = LoadParamsInFunction(item, first)
    --     temp_param[param_name] = param_data
    --   end
    --   temp_func["param"] = temp_param
    --   dest.interface[first].struct[name]=temp_func
    -- end

    k=k+1
   end
 end
 

local function LoadFunction( api, dest  )
  for first, v in pairs (dest.interface) do
    for _, s in ipairs(v.body:children("function")) do
      local name = s:attr("name")
      local msg_type = s:attr("messagetype")
      local temp_func = {}
      local temp_param = {}
      temp_func["name"] = name
      temp_func["messagetype"] = msg_type
      for _, item in ipairs(s:children("param")) do
        param_name, param_data = LoadParamsInFunction(item, first)
        temp_param[param_name] = param_data
      end

      temp_func["param"] = temp_param
      dest.interface[first].type[msg_type].functions[name]=temp_func
    end
  end
end

-- Load interfaces from api. Each function, enum and struct will be 
-- kept inside appropriate interface
local function LoadInterfaces(interfaces, dest )
  local count = xml_loader.get_count(interfaces)
  for i =0, count-1 do 
    name  = xml_loader.get_attribute_name(interfaces[i], 'name')
    print(name)
    dest.interface[name] ={}
    dest.interface[name].body = s
    dest.interface[name].type={}
    dest.interface[name].type['request']={}
    dest.interface[name].type['request'].functions={}
    dest.interface[name].type['response']={}
    dest.interface[name].type['response'].functions={}
    dest.interface[name].type['notification']={}
    dest.interface[name].type['notification'].functions={}
    dest.interface[name].enum={}
    dest.interface[name].struct={}
  end
end


 function module.init(filename)
  local result = {}
  result.interface = {}


  root = python.asattr(xml_loader.open(filename))
  if not root then error(filename .. " not found") end
 
  local interfaces = python.asindx(python.asattr
                      (xml_loader.get_attribute_structure
                        (root, 'interface')))

  LoadInterfaces(interfaces, result)
print("========================1")
    -- local _api = xml.open(path)
  LoadEnums(interfaces, result)
  LoadStructs(interfaces, result)

  -- LoadFunction(_api, result)

print("========================2")
  -- print(dump(result))
  return result
 end
 

 --Test loading from HMI API

 module.init("HMI_API.xml")

 --Test loading from MobileAPI
 -- module.init("MOBILE_API.xml")
 -- return module
