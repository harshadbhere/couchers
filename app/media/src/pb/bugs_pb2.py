# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/bugs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb/bugs.proto',
  package='org.couchers.bugs',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rpb/bugs.proto\x12\x11org.couchers.bugs\x1a\x1bgoogle/protobuf/empty.proto\"\x1e\n\x0bVersionInfo\x12\x0f\n\x07version\x18\x01 \x01(\t\"\x92\x01\n\x0cReportBugReq\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07results\x18\x04 \x01(\t\x12\x18\n\x10\x66rontend_version\x18\x05 \x01(\t\x12\x12\n\nuser_agent\x18\x06 \x01(\t\x12\x0c\n\x04page\x18\x07 \x01(\t\x12\x0f\n\x07user_id\x18\x08 \x01(\x03\"/\n\x0cReportBugRes\x12\x0e\n\x06\x62ug_id\x18\x02 \x01(\t\x12\x0f\n\x07\x62ug_url\x18\x03 \x01(\t2\x9c\x01\n\x04\x42ugs\x12\x43\n\x07Version\x12\x16.google.protobuf.Empty\x1a\x1e.org.couchers.bugs.VersionInfo\"\x00\x12O\n\tReportBug\x12\x1f.org.couchers.bugs.ReportBugReq\x1a\x1f.org.couchers.bugs.ReportBugRes\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_VERSIONINFO = _descriptor.Descriptor(
  name='VersionInfo',
  full_name='org.couchers.bugs.VersionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='org.couchers.bugs.VersionInfo.version', index=0,
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
  serialized_start=65,
  serialized_end=95,
)


_REPORTBUGREQ = _descriptor.Descriptor(
  name='ReportBugReq',
  full_name='org.couchers.bugs.ReportBugReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject', full_name='org.couchers.bugs.ReportBugReq.subject', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='org.couchers.bugs.ReportBugReq.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='org.couchers.bugs.ReportBugReq.results', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frontend_version', full_name='org.couchers.bugs.ReportBugReq.frontend_version', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='org.couchers.bugs.ReportBugReq.user_agent', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='org.couchers.bugs.ReportBugReq.page', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='org.couchers.bugs.ReportBugReq.user_id', index=6,
      number=8, type=3, cpp_type=2, label=1,
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
  serialized_start=98,
  serialized_end=244,
)


_REPORTBUGRES = _descriptor.Descriptor(
  name='ReportBugRes',
  full_name='org.couchers.bugs.ReportBugRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bug_id', full_name='org.couchers.bugs.ReportBugRes.bug_id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bug_url', full_name='org.couchers.bugs.ReportBugRes.bug_url', index=1,
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
  serialized_start=246,
  serialized_end=293,
)

DESCRIPTOR.message_types_by_name['VersionInfo'] = _VERSIONINFO
DESCRIPTOR.message_types_by_name['ReportBugReq'] = _REPORTBUGREQ
DESCRIPTOR.message_types_by_name['ReportBugRes'] = _REPORTBUGRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersionInfo = _reflection.GeneratedProtocolMessageType('VersionInfo', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONINFO,
  '__module__' : 'pb.bugs_pb2'
  # @@protoc_insertion_point(class_scope:org.couchers.bugs.VersionInfo)
  })
_sym_db.RegisterMessage(VersionInfo)

ReportBugReq = _reflection.GeneratedProtocolMessageType('ReportBugReq', (_message.Message,), {
  'DESCRIPTOR' : _REPORTBUGREQ,
  '__module__' : 'pb.bugs_pb2'
  # @@protoc_insertion_point(class_scope:org.couchers.bugs.ReportBugReq)
  })
_sym_db.RegisterMessage(ReportBugReq)

ReportBugRes = _reflection.GeneratedProtocolMessageType('ReportBugRes', (_message.Message,), {
  'DESCRIPTOR' : _REPORTBUGRES,
  '__module__' : 'pb.bugs_pb2'
  # @@protoc_insertion_point(class_scope:org.couchers.bugs.ReportBugRes)
  })
_sym_db.RegisterMessage(ReportBugRes)



_BUGS = _descriptor.ServiceDescriptor(
  name='Bugs',
  full_name='org.couchers.bugs.Bugs',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=296,
  serialized_end=452,
  methods=[
  _descriptor.MethodDescriptor(
    name='Version',
    full_name='org.couchers.bugs.Bugs.Version',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_VERSIONINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportBug',
    full_name='org.couchers.bugs.Bugs.ReportBug',
    index=1,
    containing_service=None,
    input_type=_REPORTBUGREQ,
    output_type=_REPORTBUGRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BUGS)

DESCRIPTOR.services_by_name['Bugs'] = _BUGS

# @@protoc_insertion_point(module_scope)
