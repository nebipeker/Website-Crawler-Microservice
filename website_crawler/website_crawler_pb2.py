# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: website_crawler.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15website_crawler.proto\x12\x0fwebsite_crawler\",\n\x15WebsiteCrawlerRequest\x12\x13\n\x0bwebsite_url\x18\x01 \x01(\t\"&\n\x16WebsiteCrawlerResponse\x12\x0c\n\x04urls\x18\x01 \x03(\t2z\n\x15WebsiteCrawlerService\x12\x61\n\x0c\x43rawlWebsite\x12&.website_crawler.WebsiteCrawlerRequest\x1a\'.website_crawler.WebsiteCrawlerResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'website_crawler_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEBSITECRAWLERREQUEST._serialized_start=42
  _WEBSITECRAWLERREQUEST._serialized_end=86
  _WEBSITECRAWLERRESPONSE._serialized_start=88
  _WEBSITECRAWLERRESPONSE._serialized_end=126
  _WEBSITECRAWLERSERVICE._serialized_start=128
  _WEBSITECRAWLERSERVICE._serialized_end=250
# @@protoc_insertion_point(module_scope)
