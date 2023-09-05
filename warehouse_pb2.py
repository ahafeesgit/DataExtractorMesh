# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: warehouse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fwarehouse.proto\x12&picker_account_management.warehouse.v1\x1a\x1egoogle/protobuf/wrappers.proto\"8\n\x06Status\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\"\x1c\n\x1aGetPickerWarehousesRequest\"\x9e\x07\n\x1bGetPickerWarehousesResponse\x12\x61\n\nwarehouses\x18\x01 \x03(\x0b\x32M.picker_account_management.warehouse.v1.GetPickerWarehousesResponse.Warehouse\x1a\xa5\x01\n\x06\x43onfig\x12j\n\x08property\x18\x01 \x03(\x0b\x32X.picker_account_management.warehouse.v1.GetPickerWarehousesResponse.Config.PropertyEntry\x1a/\n\rPropertyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a@\n\x05Store\x12\x18\n\x10global_entity_id\x18\x01 \x01(\t\x12\x1d\n\x15platform_warehouse_id\x18\x02 \x01(\t\x1a\xb1\x04\n\tWarehouse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x07\x61\x64\x64ress\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08latitude\x18\x04 \x01(\x01H\x01\x88\x01\x01\x12\x16\n\tlongitude\x18\x05 \x01(\x01H\x02\x88\x01\x01\x12\x16\n\timage_url\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x10\n\x08\x63hildren\x18\x07 \x03(\t\x12\x18\n\x10global_entity_id\x18\x08 \x01(\t\x12Y\n\x06stores\x18\t \x03(\x0b\x32I.picker_account_management.warehouse.v1.GetPickerWarehousesResponse.Store\x12_\n\x06\x63onfig\x18\n \x01(\x0b\x32J.picker_account_management.warehouse.v1.GetPickerWarehousesResponse.ConfigH\x04\x88\x01\x01\x12 \n\x13global_warehouse_id\x18\x0b \x01(\tH\x05\x88\x01\x01\x12K\n\rbusiness_unit\x18\x0c \x01(\x0e\x32\x34.picker_account_management.warehouse.v1.BusinessUnitB\n\n\x08_addressB\x0b\n\t_latitudeB\x0c\n\n_longitudeB\x0c\n\n_image_urlB\t\n\x07_configB\x16\n\x14_global_warehouse_id\"\x8c\x01\n\x17GetWarehouseByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10global_entity_id\x18\x02 \x01(\t\x12K\n\rbusiness_unit\x18\x03 \x01(\x0e\x32\x34.picker_account_management.warehouse.v1.BusinessUnit\"\x97\x01\n\x18GetWarehouseByIdResponse\x12\x43\n\x06status\x18\x01 \x01(\x0b\x32..picker_account_management.warehouse.v1.StatusH\x00\x88\x01\x01\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\timage_url\x18\x04 \x01(\tB\t\n\x07_status\"}\n\x14GetWarehousesRequest\x12\x18\n\x10global_entity_id\x18\x01 \x01(\t\x12K\n\rbusiness_unit\x18\x02 \x01(\x0e\x32\x34.picker_account_management.warehouse.v1.BusinessUnit\"\xbd\x01\n\x15GetWarehousesResponse\x12\x43\n\x06status\x18\x01 \x01(\x0b\x32..picker_account_management.warehouse.v1.StatusH\x00\x88\x01\x01\x12T\n\nwarehouses\x18\x02 \x03(\x0b\x32@.picker_account_management.warehouse.v1.GetWarehouseByIdResponseB\t\n\x07_status*d\n\x0c\x42usinessUnit\x12\x1d\n\x19\x42USINESS_UNIT_UNSPECIFIED\x10\x00\x12\x17\n\x13\x42USINESS_UNIT_DMART\x10\x01\x12\x1c\n\x18\x42USINESS_UNIT_LOCAL_SHOP\x10\x02\x32\xda\x03\n\x10WarehouseService\x12\x8c\x01\n\rGetWarehouses\x12<.picker_account_management.warehouse.v1.GetWarehousesRequest\x1a=.picker_account_management.warehouse.v1.GetWarehousesResponse\x12\x9e\x01\n\x13GetPickerWarehouses\x12\x42.picker_account_management.warehouse.v1.GetPickerWarehousesRequest\x1a\x43.picker_account_management.warehouse.v1.GetPickerWarehousesResponse\x12\x95\x01\n\x10GetWarehouseById\x12?.picker_account_management.warehouse.v1.GetWarehouseByIdRequest\x1a@.picker_account_management.warehouse.v1.GetWarehouseByIdResponseB\xac\x01\n<io.deliveryhero.proto.picker_account_management.warehouse.v1B\x0eWarehouseProtoP\x01ZZgithub.com/deliveryhero/dh-nv-proto-golang/packages/picker_account_management/v1/warehouseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'warehouse_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n<io.deliveryhero.proto.picker_account_management.warehouse.v1B\016WarehouseProtoP\001ZZgithub.com/deliveryhero/dh-nv-proto-golang/packages/picker_account_management/v1/warehouse'
  _GETPICKERWAREHOUSESRESPONSE_CONFIG_PROPERTYENTRY._options = None
  _GETPICKERWAREHOUSESRESPONSE_CONFIG_PROPERTYENTRY._serialized_options = b'8\001'
  _globals['_BUSINESSUNIT']._serialized_start=1724
  _globals['_BUSINESSUNIT']._serialized_end=1824
  _globals['_STATUS']._serialized_start=91
  _globals['_STATUS']._serialized_end=147
  _globals['_GETPICKERWAREHOUSESREQUEST']._serialized_start=149
  _globals['_GETPICKERWAREHOUSESREQUEST']._serialized_end=177
  _globals['_GETPICKERWAREHOUSESRESPONSE']._serialized_start=180
  _globals['_GETPICKERWAREHOUSESRESPONSE']._serialized_end=1106
  _globals['_GETPICKERWAREHOUSESRESPONSE_CONFIG']._serialized_start=311
  _globals['_GETPICKERWAREHOUSESRESPONSE_CONFIG']._serialized_end=476
  _globals['_GETPICKERWAREHOUSESRESPONSE_CONFIG_PROPERTYENTRY']._serialized_start=429
  _globals['_GETPICKERWAREHOUSESRESPONSE_CONFIG_PROPERTYENTRY']._serialized_end=476
  _globals['_GETPICKERWAREHOUSESRESPONSE_STORE']._serialized_start=478
  _globals['_GETPICKERWAREHOUSESRESPONSE_STORE']._serialized_end=542
  _globals['_GETPICKERWAREHOUSESRESPONSE_WAREHOUSE']._serialized_start=545
  _globals['_GETPICKERWAREHOUSESRESPONSE_WAREHOUSE']._serialized_end=1106
  _globals['_GETWAREHOUSEBYIDREQUEST']._serialized_start=1109
  _globals['_GETWAREHOUSEBYIDREQUEST']._serialized_end=1249
  _globals['_GETWAREHOUSEBYIDRESPONSE']._serialized_start=1252
  _globals['_GETWAREHOUSEBYIDRESPONSE']._serialized_end=1403
  _globals['_GETWAREHOUSESREQUEST']._serialized_start=1405
  _globals['_GETWAREHOUSESREQUEST']._serialized_end=1530
  _globals['_GETWAREHOUSESRESPONSE']._serialized_start=1533
  _globals['_GETWAREHOUSESRESPONSE']._serialized_end=1722
  _globals['_WAREHOUSESERVICE']._serialized_start=1827
  _globals['_WAREHOUSESERVICE']._serialized_end=2301
# @@protoc_insertion_point(module_scope)