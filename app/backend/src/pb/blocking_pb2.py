# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/blocking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb/blocking.proto',
  package='org.couchers.blocking',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11pb/blocking.proto\x12\x15org.couchers.blocking\x1a\x1bgoogle/protobuf/empty.proto\" \n\x0c\x42lockUserReq\x12\x10\n\x08username\x18\x01 \x01(\t\"\"\n\x0eUnblockUserReq\x12\x10\n\x08username\x18\x01 \x01(\t\"/\n\x12GetBlockedUsersRes\x12\x19\n\x11\x62locked_usernames\x18\x01 \x03(\t2\xfa\x01\n\x08\x42locking\x12H\n\tBlockUser\x12#.org.couchers.blocking.BlockUserReq\x1a\x16.google.protobuf.Empty\x12L\n\x0bUnblockUser\x12%.org.couchers.blocking.UnblockUserReq\x1a\x16.google.protobuf.Empty\x12V\n\x0fGetBlockedUsers\x12\x16.google.protobuf.Empty\x1a).org.couchers.blocking.GetBlockedUsersRes\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BLOCKUSERREQ = _descriptor.Descriptor(
  name='BlockUserReq',
  full_name='org.couchers.blocking.BlockUserReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='org.couchers.blocking.BlockUserReq.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=73,
  serialized_end=105,
)


_UNBLOCKUSERREQ = _descriptor.Descriptor(
  name='UnblockUserReq',
  full_name='org.couchers.blocking.UnblockUserReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='org.couchers.blocking.UnblockUserReq.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=107,
  serialized_end=141,
)


_GETBLOCKEDUSERSRES = _descriptor.Descriptor(
  name='GetBlockedUsersRes',
  full_name='org.couchers.blocking.GetBlockedUsersRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocked_usernames', full_name='org.couchers.blocking.GetBlockedUsersRes.blocked_usernames', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=143,
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['BlockUserReq'] = _BLOCKUSERREQ
DESCRIPTOR.message_types_by_name['UnblockUserReq'] = _UNBLOCKUSERREQ
DESCRIPTOR.message_types_by_name['GetBlockedUsersRes'] = _GETBLOCKEDUSERSRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockUserReq = _reflection.GeneratedProtocolMessageType('BlockUserReq', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKUSERREQ,
  '__module__' : 'pb.blocking_pb2'
  # @@protoc_insertion_point(class_scope:org.couchers.blocking.BlockUserReq)
  })
_sym_db.RegisterMessage(BlockUserReq)

UnblockUserReq = _reflection.GeneratedProtocolMessageType('UnblockUserReq', (_message.Message,), {
  'DESCRIPTOR' : _UNBLOCKUSERREQ,
  '__module__' : 'pb.blocking_pb2'
  # @@protoc_insertion_point(class_scope:org.couchers.blocking.UnblockUserReq)
  })
_sym_db.RegisterMessage(UnblockUserReq)

GetBlockedUsersRes = _reflection.GeneratedProtocolMessageType('GetBlockedUsersRes', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKEDUSERSRES,
  '__module__' : 'pb.blocking_pb2'
  # @@protoc_insertion_point(class_scope:org.couchers.blocking.GetBlockedUsersRes)
  })
_sym_db.RegisterMessage(GetBlockedUsersRes)



_BLOCKING = _descriptor.ServiceDescriptor(
  name='Blocking',
  full_name='org.couchers.blocking.Blocking',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=193,
  serialized_end=443,
  methods=[
  _descriptor.MethodDescriptor(
    name='BlockUser',
    full_name='org.couchers.blocking.Blocking.BlockUser',
    index=0,
    containing_service=None,
    input_type=_BLOCKUSERREQ,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UnblockUser',
    full_name='org.couchers.blocking.Blocking.UnblockUser',
    index=1,
    containing_service=None,
    input_type=_UNBLOCKUSERREQ,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlockedUsers',
    full_name='org.couchers.blocking.Blocking.GetBlockedUsers',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETBLOCKEDUSERSRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BLOCKING)

DESCRIPTOR.services_by_name['Blocking'] = _BLOCKING

# @@protoc_insertion_point(module_scope)
