# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import warehouse_pb2 as warehouse__pb2


class WarehouseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetWarehouses = channel.unary_unary(
                '/picker_account_management.warehouse.v1.WarehouseService/GetWarehouses',
                request_serializer=warehouse__pb2.GetWarehousesRequest.SerializeToString,
                response_deserializer=warehouse__pb2.GetWarehousesResponse.FromString,
                )
        self.GetPickerWarehouses = channel.unary_unary(
                '/picker_account_management.warehouse.v1.WarehouseService/GetPickerWarehouses',
                request_serializer=warehouse__pb2.GetPickerWarehousesRequest.SerializeToString,
                response_deserializer=warehouse__pb2.GetPickerWarehousesResponse.FromString,
                )
        self.GetWarehouseById = channel.unary_unary(
                '/picker_account_management.warehouse.v1.WarehouseService/GetWarehouseById',
                request_serializer=warehouse__pb2.GetWarehouseByIdRequest.SerializeToString,
                response_deserializer=warehouse__pb2.GetWarehouseByIdResponse.FromString,
                )


class WarehouseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetWarehouses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPickerWarehouses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWarehouseById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WarehouseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetWarehouses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWarehouses,
                    request_deserializer=warehouse__pb2.GetWarehousesRequest.FromString,
                    response_serializer=warehouse__pb2.GetWarehousesResponse.SerializeToString,
            ),
            'GetPickerWarehouses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPickerWarehouses,
                    request_deserializer=warehouse__pb2.GetPickerWarehousesRequest.FromString,
                    response_serializer=warehouse__pb2.GetPickerWarehousesResponse.SerializeToString,
            ),
            'GetWarehouseById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWarehouseById,
                    request_deserializer=warehouse__pb2.GetWarehouseByIdRequest.FromString,
                    response_serializer=warehouse__pb2.GetWarehouseByIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'picker_account_management.warehouse.v1.WarehouseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WarehouseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetWarehouses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.warehouse.v1.WarehouseService/GetWarehouses',
            warehouse__pb2.GetWarehousesRequest.SerializeToString,
            warehouse__pb2.GetWarehousesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPickerWarehouses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.warehouse.v1.WarehouseService/GetPickerWarehouses',
            warehouse__pb2.GetPickerWarehousesRequest.SerializeToString,
            warehouse__pb2.GetPickerWarehousesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWarehouseById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.warehouse.v1.WarehouseService/GetWarehouseById',
            warehouse__pb2.GetWarehouseByIdRequest.SerializeToString,
            warehouse__pb2.GetWarehouseByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
