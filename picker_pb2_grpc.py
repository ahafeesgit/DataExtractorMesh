# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import picker_pb2 as picker__pb2


class PickerAdminControllerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPickers = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerAdminControllerService/GetPickers',
                request_serializer=picker__pb2.GetPickersRequest.SerializeToString,
                response_deserializer=picker__pb2.GetPickersResponse.FromString,
                )
        self.CreatePicker = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerAdminControllerService/CreatePicker',
                request_serializer=picker__pb2.CreatePickerRequest.SerializeToString,
                response_deserializer=picker__pb2.CreatePickerResponse.FromString,
                )
        self.UpdatePicker = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerAdminControllerService/UpdatePicker',
                request_serializer=picker__pb2.UpdatePickerRequest.SerializeToString,
                response_deserializer=picker__pb2.UpdatePickerResponse.FromString,
                )
        self.CreatePickersByBulk = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerAdminControllerService/CreatePickersByBulk',
                request_serializer=picker__pb2.CreatePickersByBulkRequest.SerializeToString,
                response_deserializer=picker__pb2.CreatePickersByBulkResponse.FromString,
                )


class PickerAdminControllerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPickers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePicker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePicker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePickersByBulk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PickerAdminControllerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPickers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPickers,
                    request_deserializer=picker__pb2.GetPickersRequest.FromString,
                    response_serializer=picker__pb2.GetPickersResponse.SerializeToString,
            ),
            'CreatePicker': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePicker,
                    request_deserializer=picker__pb2.CreatePickerRequest.FromString,
                    response_serializer=picker__pb2.CreatePickerResponse.SerializeToString,
            ),
            'UpdatePicker': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePicker,
                    request_deserializer=picker__pb2.UpdatePickerRequest.FromString,
                    response_serializer=picker__pb2.UpdatePickerResponse.SerializeToString,
            ),
            'CreatePickersByBulk': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePickersByBulk,
                    request_deserializer=picker__pb2.CreatePickersByBulkRequest.FromString,
                    response_serializer=picker__pb2.CreatePickersByBulkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'picker_account_management.picker.v1.PickerAdminControllerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PickerAdminControllerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPickers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerAdminControllerService/GetPickers',
            picker__pb2.GetPickersRequest.SerializeToString,
            picker__pb2.GetPickersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePicker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerAdminControllerService/CreatePicker',
            picker__pb2.CreatePickerRequest.SerializeToString,
            picker__pb2.CreatePickerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePicker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerAdminControllerService/UpdatePicker',
            picker__pb2.UpdatePickerRequest.SerializeToString,
            picker__pb2.UpdatePickerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePickersByBulk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerAdminControllerService/CreatePickersByBulk',
            picker__pb2.CreatePickersByBulkRequest.SerializeToString,
            picker__pb2.CreatePickersByBulkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class PickerControllerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetActivePicker = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerControllerService/GetActivePicker',
                request_serializer=picker__pb2.GetActivePickerRequest.SerializeToString,
                response_deserializer=picker__pb2.GetActivePickerResponse.FromString,
                )
        self.GetPickerById = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerControllerService/GetPickerById',
                request_serializer=picker__pb2.GetPickerByIdRequest.SerializeToString,
                response_deserializer=picker__pb2.GetPickerByIdResponse.FromString,
                )
        self.GetRiderById = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerControllerService/GetRiderById',
                request_serializer=picker__pb2.GetRiderByIdRequest.SerializeToString,
                response_deserializer=picker__pb2.GetRiderByIdResponse.FromString,
                )
        self.SetInitialPasswordStatus = channel.unary_unary(
                '/picker_account_management.picker.v1.PickerControllerService/SetInitialPasswordStatus',
                request_serializer=picker__pb2.SetInitialPasswordStatusRequest.SerializeToString,
                response_deserializer=picker__pb2.SetInitialPasswordStatusResponse.FromString,
                )


class PickerControllerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetActivePicker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPickerById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRiderById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetInitialPasswordStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PickerControllerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetActivePicker': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActivePicker,
                    request_deserializer=picker__pb2.GetActivePickerRequest.FromString,
                    response_serializer=picker__pb2.GetActivePickerResponse.SerializeToString,
            ),
            'GetPickerById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPickerById,
                    request_deserializer=picker__pb2.GetPickerByIdRequest.FromString,
                    response_serializer=picker__pb2.GetPickerByIdResponse.SerializeToString,
            ),
            'GetRiderById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRiderById,
                    request_deserializer=picker__pb2.GetRiderByIdRequest.FromString,
                    response_serializer=picker__pb2.GetRiderByIdResponse.SerializeToString,
            ),
            'SetInitialPasswordStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetInitialPasswordStatus,
                    request_deserializer=picker__pb2.SetInitialPasswordStatusRequest.FromString,
                    response_serializer=picker__pb2.SetInitialPasswordStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'picker_account_management.picker.v1.PickerControllerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PickerControllerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetActivePicker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerControllerService/GetActivePicker',
            picker__pb2.GetActivePickerRequest.SerializeToString,
            picker__pb2.GetActivePickerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPickerById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerControllerService/GetPickerById',
            picker__pb2.GetPickerByIdRequest.SerializeToString,
            picker__pb2.GetPickerByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRiderById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerControllerService/GetRiderById',
            picker__pb2.GetRiderByIdRequest.SerializeToString,
            picker__pb2.GetRiderByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetInitialPasswordStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/picker_account_management.picker.v1.PickerControllerService/SetInitialPasswordStatus',
            picker__pb2.SetInitialPasswordStatusRequest.SerializeToString,
            picker__pb2.SetInitialPasswordStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
