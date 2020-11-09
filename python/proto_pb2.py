# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto.proto',
  package='api',
  syntax='proto3',
  serialized_options=b'Z\006go/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bproto.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"3\n\x06Report\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x06status\x18\x02 \x01(\x0e\x32\x0b.api.Status\"u\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\tcharacter\x18\x03 \x01(\x0e\x32\x0e.api.Character\x12\x0c\n\x04role\x18\x04 \x01(\t\x12\x11\n\treadiness\x18\x05 \x01(\x08\x12\x1b\n\x06status\x18\x06 \x01(\x0e\x32\x0b.api.Status\"\xbe\x01\n\x06Result\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.api.Result.Status\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12!\n\x06scores\x18\x04 \x03(\x0b\x32\x11.api.Result.Score\x1a$\n\x05Score\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\t\".\n\x06Status\x12\x0b\n\x07unknown\x10\x00\x12\x0b\n\x07success\x10\x01\x12\n\n\x06\x66\x61iled\x10\x02\"4\n\x03Key\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\"R\n\x04Meta\x12\x18\n\x05owner\x18\x01 \x01(\x0b\x32\t.api.User\x12\x30\n\x0c\x63reationTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x07Message\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x15\n\x03key\x18\x02 \x01(\x0b\x32\x08.api.Key\x12\x17\n\x04meta\x18\x03 \x01(\x0b\x32\t.api.Meta*T\n\tCharacter\x12\x14\n\x10unknownCharacter\x10\x00\x12\x0c\n\x08\x64irector\x10\x01\x12\t\n\x05\x61\x63tor\x10\x02\x12\x0c\n\x08operator\x10\x03\x12\n\n\x06master\x10\x04*\x9d\x01\n\x06Method\x12\x11\n\runknownMethod\x10\x00\x12\x07\n\x03Get\x10\x01\x12\n\n\x06GetAll\x10\x02\x12\x07\n\x03Put\x10\x03\x12\n\n\x06\x44\x65lete\x10\x04\x12\r\n\tDeleteAll\x10\x05\x12\t\n\x05Watch\x10\x06\x12\x11\n\rSetUserStatus\x10\n\x12\r\n\tGetActors\x10\x14\x12\r\n\tPutResult\x10\x15\x12\x0b\n\x07ImReady\x10\x1e*P\n\x06Status\x12\x11\n\runknownStatus\x10\x00\x12\x0b\n\x07unknown\x10\x01\x12\x0b\n\x07running\x10\x02\x12\r\n\tsucceeded\x10\x03\x12\n\n\x06\x66\x61iled\x10\x04\x32\xfa\x01\n\nMessageAPI\x12\x1d\n\x03Get\x12\x08.api.Key\x1a\x0c.api.Message\x12\"\n\x06GetAll\x12\x08.api.Key\x1a\x0c.api.Message0\x01\x12+\n\x03Put\x12\x0c.api.Message\x1a\x16.google.protobuf.Empty\x12*\n\x06\x44\x65lete\x12\x08.api.Key\x1a\x16.google.protobuf.Empty\x12-\n\tDeleteAll\x12\x08.api.Key\x1a\x16.google.protobuf.Empty\x12!\n\x05Watch\x12\x08.api.Key\x1a\x0c.api.Message0\x01\x32q\n\x0b\x44irectorAPI\x12\x30\n\tGetActors\x12\x16.google.protobuf.Empty\x1a\t.api.User0\x01\x12\x30\n\tPutResult\x12\x0b.api.Result\x1a\x16.google.protobuf.Empty2C\n\x0bOperatorAPI\x12\x34\n\rSetUserStatus\x12\x0b.api.Report\x1a\x16.google.protobuf.Empty2|\n\x07UserAPI\x12\x39\n\x07ImReady\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12\x36\n\x04Ping\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.EmptyB\x08Z\x06go/apib\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_CHARACTER = _descriptor.EnumDescriptor(
  name='Character',
  full_name='api.Character',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknownCharacter', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='director', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='actor', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='operator', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='master', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=661,
  serialized_end=745,
)
_sym_db.RegisterEnumDescriptor(_CHARACTER)

Character = enum_type_wrapper.EnumTypeWrapper(_CHARACTER)
_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='api.Method',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknownMethod', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Get', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GetAll', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Put', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Delete', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DeleteAll', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Watch', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SetUserStatus', index=7, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GetActors', index=8, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PutResult', index=9, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ImReady', index=10, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=748,
  serialized_end=905,
)
_sym_db.RegisterEnumDescriptor(_METHOD)

Method = enum_type_wrapper.EnumTypeWrapper(_METHOD)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='api.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknownStatus', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='running', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='succeeded', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='failed', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=907,
  serialized_end=987,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
unknownCharacter = 0
director = 1
actor = 2
operator = 3
master = 4
unknownMethod = 0
Get = 1
GetAll = 2
Put = 3
Delete = 4
DeleteAll = 5
Watch = 6
SetUserStatus = 10
GetActors = 20
PutResult = 21
ImReady = 30
unknownStatus = 0
unknown = 1
running = 2
succeeded = 3
failed = 4


_RESULT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='api.Result.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='success', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='failed', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=399,
  serialized_end=445,
)
_sym_db.RegisterEnumDescriptor(_RESULT_STATUS)


_REPORT = _descriptor.Descriptor(
  name='Report',
  full_name='api.Report',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Report.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.Report.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=133,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='api.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='character', full_name='api.User.character', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='api.User.role', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='readiness', full_name='api.User.readiness', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.User.status', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=252,
)


_RESULT_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='api.Result.Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Result.Score.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='api.Result.Score.score', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=397,
)

_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='api.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.Result.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.Result.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='api.Result.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='api.Result.scores', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_SCORE, ],
  enum_types=[
    _RESULT_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=445,
)


_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='api.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='api.Key.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Key.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='api.Key.namespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=499,
)


_META = _descriptor.Descriptor(
  name='Meta',
  full_name='api.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='api.Meta.owner', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creationTime', full_name='api.Meta.creationTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=583,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='api.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='api.Message.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='api.Message.key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='api.Message.meta', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=659,
)

_REPORT.fields_by_name['status'].enum_type = _STATUS
_USER.fields_by_name['character'].enum_type = _CHARACTER
_USER.fields_by_name['status'].enum_type = _STATUS
_RESULT_SCORE.containing_type = _RESULT
_RESULT.fields_by_name['status'].enum_type = _RESULT_STATUS
_RESULT.fields_by_name['scores'].message_type = _RESULT_SCORE
_RESULT_STATUS.containing_type = _RESULT
_META.fields_by_name['owner'].message_type = _USER
_META.fields_by_name['creationTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MESSAGE.fields_by_name['key'].message_type = _KEY
_MESSAGE.fields_by_name['meta'].message_type = _META
DESCRIPTOR.message_types_by_name['Report'] = _REPORT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['Key'] = _KEY
DESCRIPTOR.message_types_by_name['Meta'] = _META
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['Character'] = _CHARACTER
DESCRIPTOR.enum_types_by_name['Method'] = _METHOD
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Report = _reflection.GeneratedProtocolMessageType('Report', (_message.Message,), {
  'DESCRIPTOR' : _REPORT,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:api.Report)
  })
_sym_db.RegisterMessage(Report)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:api.User)
  })
_sym_db.RegisterMessage(User)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {

  'Score' : _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), {
    'DESCRIPTOR' : _RESULT_SCORE,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:api.Result.Score)
    })
  ,
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:api.Result)
  })
_sym_db.RegisterMessage(Result)
_sym_db.RegisterMessage(Result.Score)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:api.Key)
  })
_sym_db.RegisterMessage(Key)

Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), {
  'DESCRIPTOR' : _META,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:api.Meta)
  })
_sym_db.RegisterMessage(Meta)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:api.Message)
  })
_sym_db.RegisterMessage(Message)


DESCRIPTOR._options = None

_MESSAGEAPI = _descriptor.ServiceDescriptor(
  name='MessageAPI',
  full_name='api.MessageAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=990,
  serialized_end=1240,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='api.MessageAPI.Get',
    index=0,
    containing_service=None,
    input_type=_KEY,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAll',
    full_name='api.MessageAPI.GetAll',
    index=1,
    containing_service=None,
    input_type=_KEY,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Put',
    full_name='api.MessageAPI.Put',
    index=2,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='api.MessageAPI.Delete',
    index=3,
    containing_service=None,
    input_type=_KEY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAll',
    full_name='api.MessageAPI.DeleteAll',
    index=4,
    containing_service=None,
    input_type=_KEY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Watch',
    full_name='api.MessageAPI.Watch',
    index=5,
    containing_service=None,
    input_type=_KEY,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGEAPI)

DESCRIPTOR.services_by_name['MessageAPI'] = _MESSAGEAPI


_DIRECTORAPI = _descriptor.ServiceDescriptor(
  name='DirectorAPI',
  full_name='api.DirectorAPI',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1242,
  serialized_end=1355,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetActors',
    full_name='api.DirectorAPI.GetActors',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PutResult',
    full_name='api.DirectorAPI.PutResult',
    index=1,
    containing_service=None,
    input_type=_RESULT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIRECTORAPI)

DESCRIPTOR.services_by_name['DirectorAPI'] = _DIRECTORAPI


_OPERATORAPI = _descriptor.ServiceDescriptor(
  name='OperatorAPI',
  full_name='api.OperatorAPI',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1357,
  serialized_end=1424,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetUserStatus',
    full_name='api.OperatorAPI.SetUserStatus',
    index=0,
    containing_service=None,
    input_type=_REPORT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OPERATORAPI)

DESCRIPTOR.services_by_name['OperatorAPI'] = _OPERATORAPI


_USERAPI = _descriptor.ServiceDescriptor(
  name='UserAPI',
  full_name='api.UserAPI',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1426,
  serialized_end=1550,
  methods=[
  _descriptor.MethodDescriptor(
    name='ImReady',
    full_name='api.UserAPI.ImReady',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='api.UserAPI.Ping',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERAPI)

DESCRIPTOR.services_by_name['UserAPI'] = _USERAPI

# @@protoc_insertion_point(module_scope)
