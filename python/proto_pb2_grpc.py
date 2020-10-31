# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import proto_pb2 as proto__pb2


class MessageAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/api.MessageAPI/Get',
                request_serializer=proto__pb2.Key.SerializeToString,
                response_deserializer=proto__pb2.Message.FromString,
                )
        self.GetAll = channel.unary_stream(
                '/api.MessageAPI/GetAll',
                request_serializer=proto__pb2.Key.SerializeToString,
                response_deserializer=proto__pb2.Message.FromString,
                )
        self.Put = channel.unary_unary(
                '/api.MessageAPI/Put',
                request_serializer=proto__pb2.Message.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Delete = channel.unary_unary(
                '/api.MessageAPI/Delete',
                request_serializer=proto__pb2.Key.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteAll = channel.unary_unary(
                '/api.MessageAPI/DeleteAll',
                request_serializer=proto__pb2.Key.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Watch = channel.unary_stream(
                '/api.MessageAPI/Watch',
                request_serializer=proto__pb2.Key.SerializeToString,
                response_deserializer=proto__pb2.Message.FromString,
                )


class MessageAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Put(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Watch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=proto__pb2.Key.FromString,
                    response_serializer=proto__pb2.Message.SerializeToString,
            ),
            'GetAll': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=proto__pb2.Key.FromString,
                    response_serializer=proto__pb2.Message.SerializeToString,
            ),
            'Put': grpc.unary_unary_rpc_method_handler(
                    servicer.Put,
                    request_deserializer=proto__pb2.Message.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=proto__pb2.Key.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=proto__pb2.Key.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Watch': grpc.unary_stream_rpc_method_handler(
                    servicer.Watch,
                    request_deserializer=proto__pb2.Key.FromString,
                    response_serializer=proto__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.MessageAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.MessageAPI/Get',
            proto__pb2.Key.SerializeToString,
            proto__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.MessageAPI/GetAll',
            proto__pb2.Key.SerializeToString,
            proto__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Put(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.MessageAPI/Put',
            proto__pb2.Message.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.MessageAPI/Delete',
            proto__pb2.Key.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.MessageAPI/DeleteAll',
            proto__pb2.Key.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Watch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.MessageAPI/Watch',
            proto__pb2.Key.SerializeToString,
            proto__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DirectorAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetActorWithID = channel.unary_unary(
                '/api.DirectorAPI/GetActorWithID',
                request_serializer=proto__pb2.ID.SerializeToString,
                response_deserializer=proto__pb2.Actor.FromString,
                )
        self.GetActorsWithRole = channel.unary_stream(
                '/api.DirectorAPI/GetActorsWithRole',
                request_serializer=proto__pb2.Role.SerializeToString,
                response_deserializer=proto__pb2.Actor.FromString,
                )
        self.GetAllActors = channel.unary_stream(
                '/api.DirectorAPI/GetAllActors',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=proto__pb2.Actor.FromString,
                )
        self.PutResult = channel.unary_unary(
                '/api.DirectorAPI/PutResult',
                request_serializer=proto__pb2.Result.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class DirectorAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetActorWithID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActorsWithRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllActors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DirectorAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetActorWithID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActorWithID,
                    request_deserializer=proto__pb2.ID.FromString,
                    response_serializer=proto__pb2.Actor.SerializeToString,
            ),
            'GetActorsWithRole': grpc.unary_stream_rpc_method_handler(
                    servicer.GetActorsWithRole,
                    request_deserializer=proto__pb2.Role.FromString,
                    response_serializer=proto__pb2.Actor.SerializeToString,
            ),
            'GetAllActors': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllActors,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=proto__pb2.Actor.SerializeToString,
            ),
            'PutResult': grpc.unary_unary_rpc_method_handler(
                    servicer.PutResult,
                    request_deserializer=proto__pb2.Result.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.DirectorAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DirectorAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetActorWithID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DirectorAPI/GetActorWithID',
            proto__pb2.ID.SerializeToString,
            proto__pb2.Actor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActorsWithRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.DirectorAPI/GetActorsWithRole',
            proto__pb2.Role.SerializeToString,
            proto__pb2.Actor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllActors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.DirectorAPI/GetAllActors',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            proto__pb2.Actor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.DirectorAPI/PutResult',
            proto__pb2.Result.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class OperatorAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetStatusUnknown = channel.unary_unary(
                '/api.OperatorAPI/SetStatusUnknown',
                request_serializer=proto__pb2.ID.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetStatusRunning = channel.unary_unary(
                '/api.OperatorAPI/SetStatusRunning',
                request_serializer=proto__pb2.ID.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetStatusFailed = channel.unary_unary(
                '/api.OperatorAPI/SetStatusFailed',
                request_serializer=proto__pb2.ID.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class OperatorAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetStatusUnknown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetStatusRunning(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetStatusFailed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperatorAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetStatusUnknown': grpc.unary_unary_rpc_method_handler(
                    servicer.SetStatusUnknown,
                    request_deserializer=proto__pb2.ID.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetStatusRunning': grpc.unary_unary_rpc_method_handler(
                    servicer.SetStatusRunning,
                    request_deserializer=proto__pb2.ID.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetStatusFailed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetStatusFailed,
                    request_deserializer=proto__pb2.ID.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.OperatorAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OperatorAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetStatusUnknown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OperatorAPI/SetStatusUnknown',
            proto__pb2.ID.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetStatusRunning(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OperatorAPI/SetStatusRunning',
            proto__pb2.ID.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetStatusFailed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OperatorAPI/SetStatusFailed',
            proto__pb2.ID.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ActorAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ImAmReady = channel.unary_unary(
                '/api.ActorAPI/ImAmReady',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ActorAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ImAmReady(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ActorAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ImAmReady': grpc.unary_unary_rpc_method_handler(
                    servicer.ImAmReady,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.ActorAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ActorAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ImAmReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.ActorAPI/ImAmReady',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
