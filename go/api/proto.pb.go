// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.23.0
// 	protoc        v3.13.0
// source: proto.proto

package api

import (
	proto "github.com/golang/protobuf/proto"
	empty "github.com/golang/protobuf/ptypes/empty"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type Character int32

const (
	Character_unknownCharacter Character = 0
	Character_director         Character = 1
	Character_actor            Character = 2
	Character_operator         Character = 3
	Character_master           Character = 4
)

// Enum value maps for Character.
var (
	Character_name = map[int32]string{
		0: "unknownCharacter",
		1: "director",
		2: "actor",
		3: "operator",
		4: "master",
	}
	Character_value = map[string]int32{
		"unknownCharacter": 0,
		"director":         1,
		"actor":            2,
		"operator":         3,
		"master":           4,
	}
)

func (x Character) Enum() *Character {
	p := new(Character)
	*p = x
	return p
}

func (x Character) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Character) Descriptor() protoreflect.EnumDescriptor {
	return file_proto_proto_enumTypes[0].Descriptor()
}

func (Character) Type() protoreflect.EnumType {
	return &file_proto_proto_enumTypes[0]
}

func (x Character) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Character.Descriptor instead.
func (Character) EnumDescriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{0}
}

type Method int32

const (
	Method_unknownMethod        Method = 0
	Method_Get                  Method = 1
	Method_GetAll               Method = 2
	Method_Put                  Method = 3
	Method_Delete               Method = 4
	Method_DeleteAll            Method = 5
	Method_Watch                Method = 6
	Method_SetUserStatusUnknown Method = 7
	Method_SetUserStatusRunning Method = 8
	Method_SetUserStatusFailed  Method = 9
	Method_GetActorWithID       Method = 10
	Method_GetActorsWithRole    Method = 11
	Method_GetAllActors         Method = 12
	Method_PutResult            Method = 13
	Method_ImReady              Method = 14
)

// Enum value maps for Method.
var (
	Method_name = map[int32]string{
		0:  "unknownMethod",
		1:  "Get",
		2:  "GetAll",
		3:  "Put",
		4:  "Delete",
		5:  "DeleteAll",
		6:  "Watch",
		7:  "SetUserStatusUnknown",
		8:  "SetUserStatusRunning",
		9:  "SetUserStatusFailed",
		10: "GetActorWithID",
		11: "GetActorsWithRole",
		12: "GetAllActors",
		13: "PutResult",
		14: "ImReady",
	}
	Method_value = map[string]int32{
		"unknownMethod":        0,
		"Get":                  1,
		"GetAll":               2,
		"Put":                  3,
		"Delete":               4,
		"DeleteAll":            5,
		"Watch":                6,
		"SetUserStatusUnknown": 7,
		"SetUserStatusRunning": 8,
		"SetUserStatusFailed":  9,
		"GetActorWithID":       10,
		"GetActorsWithRole":    11,
		"GetAllActors":         12,
		"PutResult":            13,
		"ImReady":              14,
	}
)

func (x Method) Enum() *Method {
	p := new(Method)
	*p = x
	return p
}

func (x Method) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Method) Descriptor() protoreflect.EnumDescriptor {
	return file_proto_proto_enumTypes[1].Descriptor()
}

func (Method) Type() protoreflect.EnumType {
	return &file_proto_proto_enumTypes[1]
}

func (x Method) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Method.Descriptor instead.
func (Method) EnumDescriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{1}
}

type Status int32

const (
	Status_unknownStatus Status = 0
	Status_unknown       Status = 1
	Status_running       Status = 2
	Status_failed        Status = 3
)

// Enum value maps for Status.
var (
	Status_name = map[int32]string{
		0: "unknownStatus",
		1: "unknown",
		2: "running",
		3: "failed",
	}
	Status_value = map[string]int32{
		"unknownStatus": 0,
		"unknown":       1,
		"running":       2,
		"failed":        3,
	}
)

func (x Status) Enum() *Status {
	p := new(Status)
	*p = x
	return p
}

func (x Status) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Status) Descriptor() protoreflect.EnumDescriptor {
	return file_proto_proto_enumTypes[2].Descriptor()
}

func (Status) Type() protoreflect.EnumType {
	return &file_proto_proto_enumTypes[2]
}

func (x Status) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Status.Descriptor instead.
func (Status) EnumDescriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{2}
}

type Key struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Type      string `protobuf:"bytes,1,opt,name=type,proto3" json:"type,omitempty"`
	Name      string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Namespace string `protobuf:"bytes,3,opt,name=namespace,proto3" json:"namespace,omitempty"`
}

func (x *Key) Reset() {
	*x = Key{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Key) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Key) ProtoMessage() {}

func (x *Key) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Key.ProtoReflect.Descriptor instead.
func (*Key) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{0}
}

func (x *Key) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

func (x *Key) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *Key) GetNamespace() string {
	if x != nil {
		return x.Namespace
	}
	return ""
}

type Meta struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Owner        string               `protobuf:"bytes,1,opt,name=owner,proto3" json:"owner,omitempty"`
	CreationTime *timestamp.Timestamp `protobuf:"bytes,2,opt,name=creationTime,proto3" json:"creationTime,omitempty"`
	Character    Character            `protobuf:"varint,3,opt,name=character,proto3,enum=api.Character" json:"character,omitempty"`
	Role         string               `protobuf:"bytes,4,opt,name=role,proto3" json:"role,omitempty"`
}

func (x *Meta) Reset() {
	*x = Meta{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Meta) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Meta) ProtoMessage() {}

func (x *Meta) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Meta.ProtoReflect.Descriptor instead.
func (*Meta) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{1}
}

func (x *Meta) GetOwner() string {
	if x != nil {
		return x.Owner
	}
	return ""
}

func (x *Meta) GetCreationTime() *timestamp.Timestamp {
	if x != nil {
		return x.CreationTime
	}
	return nil
}

func (x *Meta) GetCharacter() Character {
	if x != nil {
		return x.Character
	}
	return Character_unknownCharacter
}

func (x *Meta) GetRole() string {
	if x != nil {
		return x.Role
	}
	return ""
}

type Message struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Content string `protobuf:"bytes,1,opt,name=content,proto3" json:"content,omitempty"`
	Key     *Key   `protobuf:"bytes,2,opt,name=key,proto3" json:"key,omitempty"`
	Meta    *Meta  `protobuf:"bytes,3,opt,name=meta,proto3" json:"meta,omitempty"`
}

func (x *Message) Reset() {
	*x = Message{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Message) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Message) ProtoMessage() {}

func (x *Message) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Message.ProtoReflect.Descriptor instead.
func (*Message) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{2}
}

func (x *Message) GetContent() string {
	if x != nil {
		return x.Content
	}
	return ""
}

func (x *Message) GetKey() *Key {
	if x != nil {
		return x.Key
	}
	return nil
}

func (x *Message) GetMeta() *Meta {
	if x != nil {
		return x.Meta
	}
	return nil
}

type Name struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
}

func (x *Name) Reset() {
	*x = Name{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Name) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Name) ProtoMessage() {}

func (x *Name) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Name.ProtoReflect.Descriptor instead.
func (*Name) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{3}
}

func (x *Name) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type Role struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Role string `protobuf:"bytes,1,opt,name=role,proto3" json:"role,omitempty"`
}

func (x *Role) Reset() {
	*x = Role{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Role) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Role) ProtoMessage() {}

func (x *Role) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Role.ProtoReflect.Descriptor instead.
func (*Role) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{4}
}

func (x *Role) GetRole() string {
	if x != nil {
		return x.Role
	}
	return ""
}

type Actor struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name      string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Role      string `protobuf:"bytes,2,opt,name=role,proto3" json:"role,omitempty"`
	Readiness bool   `protobuf:"varint,3,opt,name=readiness,proto3" json:"readiness,omitempty"`
	Status    Status `protobuf:"varint,4,opt,name=status,proto3,enum=api.Status" json:"status,omitempty"`
}

func (x *Actor) Reset() {
	*x = Actor{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Actor) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Actor) ProtoMessage() {}

func (x *Actor) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Actor.ProtoReflect.Descriptor instead.
func (*Actor) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{5}
}

func (x *Actor) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *Actor) GetRole() string {
	if x != nil {
		return x.Role
	}
	return ""
}

func (x *Actor) GetReadiness() bool {
	if x != nil {
		return x.Readiness
	}
	return false
}

func (x *Actor) GetStatus() Status {
	if x != nil {
		return x.Status
	}
	return Status_unknownStatus
}

type Result struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *Result) Reset() {
	*x = Result{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Result) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Result) ProtoMessage() {}

func (x *Result) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Result.ProtoReflect.Descriptor instead.
func (*Result) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{6}
}

type User struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name      string    `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Token     string    `protobuf:"bytes,2,opt,name=token,proto3" json:"token,omitempty"`
	Character Character `protobuf:"varint,3,opt,name=character,proto3,enum=api.Character" json:"character,omitempty"`
	Role      string    `protobuf:"bytes,4,opt,name=role,proto3" json:"role,omitempty"`
	Readiness bool      `protobuf:"varint,5,opt,name=readiness,proto3" json:"readiness,omitempty"`
	Status    Status    `protobuf:"varint,6,opt,name=status,proto3,enum=api.Status" json:"status,omitempty"`
}

func (x *User) Reset() {
	*x = User{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *User) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*User) ProtoMessage() {}

func (x *User) ProtoReflect() protoreflect.Message {
	mi := &file_proto_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use User.ProtoReflect.Descriptor instead.
func (*User) Descriptor() ([]byte, []int) {
	return file_proto_proto_rawDescGZIP(), []int{7}
}

func (x *User) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *User) GetToken() string {
	if x != nil {
		return x.Token
	}
	return ""
}

func (x *User) GetCharacter() Character {
	if x != nil {
		return x.Character
	}
	return Character_unknownCharacter
}

func (x *User) GetRole() string {
	if x != nil {
		return x.Role
	}
	return ""
}

func (x *User) GetReadiness() bool {
	if x != nil {
		return x.Readiness
	}
	return false
}

func (x *User) GetStatus() Status {
	if x != nil {
		return x.Status
	}
	return Status_unknownStatus
}

var File_proto_proto protoreflect.FileDescriptor

var file_proto_proto_rawDesc = []byte{
	0x0a, 0x0b, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x03, 0x61,
	0x70, 0x69, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x22, 0x4b, 0x0a, 0x03, 0x4b, 0x65, 0x79, 0x12, 0x12, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12,
	0x1c, 0x0a, 0x09, 0x6e, 0x61, 0x6d, 0x65, 0x73, 0x70, 0x61, 0x63, 0x65, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x09, 0x6e, 0x61, 0x6d, 0x65, 0x73, 0x70, 0x61, 0x63, 0x65, 0x22, 0x9e, 0x01,
	0x0a, 0x04, 0x4d, 0x65, 0x74, 0x61, 0x12, 0x14, 0x0a, 0x05, 0x6f, 0x77, 0x6e, 0x65, 0x72, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x6f, 0x77, 0x6e, 0x65, 0x72, 0x12, 0x3e, 0x0a, 0x0c,
	0x63, 0x72, 0x65, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x69, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x0c,
	0x63, 0x72, 0x65, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x69, 0x6d, 0x65, 0x12, 0x2c, 0x0a, 0x09,
	0x63, 0x68, 0x61, 0x72, 0x61, 0x63, 0x74, 0x65, 0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0e, 0x32,
	0x0e, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x43, 0x68, 0x61, 0x72, 0x61, 0x63, 0x74, 0x65, 0x72, 0x52,
	0x09, 0x63, 0x68, 0x61, 0x72, 0x61, 0x63, 0x74, 0x65, 0x72, 0x12, 0x12, 0x0a, 0x04, 0x72, 0x6f,
	0x6c, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x72, 0x6f, 0x6c, 0x65, 0x22, 0x5e,
	0x0a, 0x07, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x18, 0x0a, 0x07, 0x63, 0x6f, 0x6e,
	0x74, 0x65, 0x6e, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x63, 0x6f, 0x6e, 0x74,
	0x65, 0x6e, 0x74, 0x12, 0x1a, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x08, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4b, 0x65, 0x79, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12,
	0x1d, 0x0a, 0x04, 0x6d, 0x65, 0x74, 0x61, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x09, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x4d, 0x65, 0x74, 0x61, 0x52, 0x04, 0x6d, 0x65, 0x74, 0x61, 0x22, 0x1a,
	0x0a, 0x04, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0x1a, 0x0a, 0x04, 0x52, 0x6f,
	0x6c, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x72, 0x6f, 0x6c, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x04, 0x72, 0x6f, 0x6c, 0x65, 0x22, 0x72, 0x0a, 0x05, 0x41, 0x63, 0x74, 0x6f, 0x72, 0x12,
	0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x72, 0x6f, 0x6c, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x04, 0x72, 0x6f, 0x6c, 0x65, 0x12, 0x1c, 0x0a, 0x09, 0x72, 0x65, 0x61, 0x64, 0x69,
	0x6e, 0x65, 0x73, 0x73, 0x18, 0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x72, 0x65, 0x61, 0x64,
	0x69, 0x6e, 0x65, 0x73, 0x73, 0x12, 0x23, 0x0a, 0x06, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x18,
	0x04, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x0b, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x53, 0x74, 0x61, 0x74,
	0x75, 0x73, 0x52, 0x06, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x22, 0x08, 0x0a, 0x06, 0x52, 0x65,
	0x73, 0x75, 0x6c, 0x74, 0x22, 0xb5, 0x01, 0x0a, 0x04, 0x55, 0x73, 0x65, 0x72, 0x12, 0x12, 0x0a,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x12, 0x14, 0x0a, 0x05, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x05, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x12, 0x2c, 0x0a, 0x09, 0x63, 0x68, 0x61, 0x72, 0x61,
	0x63, 0x74, 0x65, 0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x0e, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x43, 0x68, 0x61, 0x72, 0x61, 0x63, 0x74, 0x65, 0x72, 0x52, 0x09, 0x63, 0x68, 0x61, 0x72,
	0x61, 0x63, 0x74, 0x65, 0x72, 0x12, 0x12, 0x0a, 0x04, 0x72, 0x6f, 0x6c, 0x65, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x04, 0x72, 0x6f, 0x6c, 0x65, 0x12, 0x1c, 0x0a, 0x09, 0x72, 0x65, 0x61,
	0x64, 0x69, 0x6e, 0x65, 0x73, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x72, 0x65,
	0x61, 0x64, 0x69, 0x6e, 0x65, 0x73, 0x73, 0x12, 0x23, 0x0a, 0x06, 0x73, 0x74, 0x61, 0x74, 0x75,
	0x73, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x0b, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x53, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x52, 0x06, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x2a, 0x54, 0x0a, 0x09,
	0x43, 0x68, 0x61, 0x72, 0x61, 0x63, 0x74, 0x65, 0x72, 0x12, 0x14, 0x0a, 0x10, 0x75, 0x6e, 0x6b,
	0x6e, 0x6f, 0x77, 0x6e, 0x43, 0x68, 0x61, 0x72, 0x61, 0x63, 0x74, 0x65, 0x72, 0x10, 0x00, 0x12,
	0x0c, 0x0a, 0x08, 0x64, 0x69, 0x72, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x10, 0x01, 0x12, 0x09, 0x0a,
	0x05, 0x61, 0x63, 0x74, 0x6f, 0x72, 0x10, 0x02, 0x12, 0x0c, 0x0a, 0x08, 0x6f, 0x70, 0x65, 0x72,
	0x61, 0x74, 0x6f, 0x72, 0x10, 0x03, 0x12, 0x0a, 0x0a, 0x06, 0x6d, 0x61, 0x73, 0x74, 0x65, 0x72,
	0x10, 0x04, 0x2a, 0x85, 0x02, 0x0a, 0x06, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x12, 0x11, 0x0a,
	0x0d, 0x75, 0x6e, 0x6b, 0x6e, 0x6f, 0x77, 0x6e, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x10, 0x00,
	0x12, 0x07, 0x0a, 0x03, 0x47, 0x65, 0x74, 0x10, 0x01, 0x12, 0x0a, 0x0a, 0x06, 0x47, 0x65, 0x74,
	0x41, 0x6c, 0x6c, 0x10, 0x02, 0x12, 0x07, 0x0a, 0x03, 0x50, 0x75, 0x74, 0x10, 0x03, 0x12, 0x0a,
	0x0a, 0x06, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x10, 0x04, 0x12, 0x0d, 0x0a, 0x09, 0x44, 0x65,
	0x6c, 0x65, 0x74, 0x65, 0x41, 0x6c, 0x6c, 0x10, 0x05, 0x12, 0x09, 0x0a, 0x05, 0x57, 0x61, 0x74,
	0x63, 0x68, 0x10, 0x06, 0x12, 0x18, 0x0a, 0x14, 0x53, 0x65, 0x74, 0x55, 0x73, 0x65, 0x72, 0x53,
	0x74, 0x61, 0x74, 0x75, 0x73, 0x55, 0x6e, 0x6b, 0x6e, 0x6f, 0x77, 0x6e, 0x10, 0x07, 0x12, 0x18,
	0x0a, 0x14, 0x53, 0x65, 0x74, 0x55, 0x73, 0x65, 0x72, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52,
	0x75, 0x6e, 0x6e, 0x69, 0x6e, 0x67, 0x10, 0x08, 0x12, 0x17, 0x0a, 0x13, 0x53, 0x65, 0x74, 0x55,
	0x73, 0x65, 0x72, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x46, 0x61, 0x69, 0x6c, 0x65, 0x64, 0x10,
	0x09, 0x12, 0x12, 0x0a, 0x0e, 0x47, 0x65, 0x74, 0x41, 0x63, 0x74, 0x6f, 0x72, 0x57, 0x69, 0x74,
	0x68, 0x49, 0x44, 0x10, 0x0a, 0x12, 0x15, 0x0a, 0x11, 0x47, 0x65, 0x74, 0x41, 0x63, 0x74, 0x6f,
	0x72, 0x73, 0x57, 0x69, 0x74, 0x68, 0x52, 0x6f, 0x6c, 0x65, 0x10, 0x0b, 0x12, 0x10, 0x0a, 0x0c,
	0x47, 0x65, 0x74, 0x41, 0x6c, 0x6c, 0x41, 0x63, 0x74, 0x6f, 0x72, 0x73, 0x10, 0x0c, 0x12, 0x0d,
	0x0a, 0x09, 0x50, 0x75, 0x74, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x10, 0x0d, 0x12, 0x0b, 0x0a,
	0x07, 0x49, 0x6d, 0x52, 0x65, 0x61, 0x64, 0x79, 0x10, 0x0e, 0x2a, 0x41, 0x0a, 0x06, 0x53, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x12, 0x11, 0x0a, 0x0d, 0x75, 0x6e, 0x6b, 0x6e, 0x6f, 0x77, 0x6e, 0x53,
	0x74, 0x61, 0x74, 0x75, 0x73, 0x10, 0x00, 0x12, 0x0b, 0x0a, 0x07, 0x75, 0x6e, 0x6b, 0x6e, 0x6f,
	0x77, 0x6e, 0x10, 0x01, 0x12, 0x0b, 0x0a, 0x07, 0x72, 0x75, 0x6e, 0x6e, 0x69, 0x6e, 0x67, 0x10,
	0x02, 0x12, 0x0a, 0x0a, 0x06, 0x66, 0x61, 0x69, 0x6c, 0x65, 0x64, 0x10, 0x03, 0x32, 0xfa, 0x01,
	0x0a, 0x0a, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x41, 0x50, 0x49, 0x12, 0x1d, 0x0a, 0x03,
	0x47, 0x65, 0x74, 0x12, 0x08, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4b, 0x65, 0x79, 0x1a, 0x0c, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x22, 0x0a, 0x06, 0x47,
	0x65, 0x74, 0x41, 0x6c, 0x6c, 0x12, 0x08, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4b, 0x65, 0x79, 0x1a,
	0x0c, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x30, 0x01, 0x12,
	0x2b, 0x0a, 0x03, 0x50, 0x75, 0x74, 0x12, 0x0c, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4d, 0x65, 0x73,
	0x73, 0x61, 0x67, 0x65, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x12, 0x2a, 0x0a, 0x06,
	0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x12, 0x08, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4b, 0x65, 0x79,
	0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x12, 0x2d, 0x0a, 0x09, 0x44, 0x65, 0x6c, 0x65,
	0x74, 0x65, 0x41, 0x6c, 0x6c, 0x12, 0x08, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4b, 0x65, 0x79, 0x1a,
	0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x12, 0x21, 0x0a, 0x05, 0x57, 0x61, 0x74, 0x63, 0x68,
	0x12, 0x08, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4b, 0x65, 0x79, 0x1a, 0x0c, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x30, 0x01, 0x32, 0xce, 0x01, 0x0a, 0x0b, 0x44,
	0x69, 0x72, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x41, 0x50, 0x49, 0x12, 0x29, 0x0a, 0x10, 0x47, 0x65,
	0x74, 0x41, 0x63, 0x74, 0x6f, 0x72, 0x57, 0x69, 0x74, 0x68, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x09,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4e, 0x61, 0x6d, 0x65, 0x1a, 0x0a, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x41, 0x63, 0x74, 0x6f, 0x72, 0x12, 0x2c, 0x0a, 0x11, 0x47, 0x65, 0x74, 0x41, 0x63, 0x74, 0x6f,
	0x72, 0x73, 0x57, 0x69, 0x74, 0x68, 0x52, 0x6f, 0x6c, 0x65, 0x12, 0x09, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x52, 0x6f, 0x6c, 0x65, 0x1a, 0x0a, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x41, 0x63, 0x74, 0x6f,
	0x72, 0x30, 0x01, 0x12, 0x34, 0x0a, 0x0c, 0x47, 0x65, 0x74, 0x41, 0x6c, 0x6c, 0x41, 0x63, 0x74,
	0x6f, 0x72, 0x73, 0x12, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x1a, 0x0a, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x41, 0x63, 0x74, 0x6f, 0x72, 0x30, 0x01, 0x12, 0x30, 0x0a, 0x09, 0x50, 0x75, 0x74,
	0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x12, 0x0b, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x52, 0x65, 0x73,
	0x75, 0x6c, 0x74, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x32, 0xbd, 0x01, 0x0a, 0x0b,
	0x4f, 0x70, 0x65, 0x72, 0x61, 0x74, 0x6f, 0x72, 0x41, 0x50, 0x49, 0x12, 0x39, 0x0a, 0x14, 0x53,
	0x65, 0x74, 0x55, 0x73, 0x65, 0x72, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x55, 0x6e, 0x6b, 0x6e,
	0x6f, 0x77, 0x6e, 0x12, 0x09, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4e, 0x61, 0x6d, 0x65, 0x1a, 0x16,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x12, 0x39, 0x0a, 0x14, 0x53, 0x65, 0x74, 0x55, 0x73, 0x65,
	0x72, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x75, 0x6e, 0x6e, 0x69, 0x6e, 0x67, 0x12, 0x09,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4e, 0x61, 0x6d, 0x65, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74,
	0x79, 0x12, 0x38, 0x0a, 0x13, 0x53, 0x65, 0x74, 0x55, 0x73, 0x65, 0x72, 0x53, 0x74, 0x61, 0x74,
	0x75, 0x73, 0x46, 0x61, 0x69, 0x6c, 0x65, 0x64, 0x12, 0x09, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x4e,
	0x61, 0x6d, 0x65, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x32, 0x44, 0x0a, 0x07, 0x55,
	0x73, 0x65, 0x72, 0x41, 0x50, 0x49, 0x12, 0x39, 0x0a, 0x07, 0x49, 0x6d, 0x52, 0x65, 0x61, 0x64,
	0x79, 0x12, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74,
	0x79, 0x42, 0x08, 0x5a, 0x06, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_proto_proto_rawDescOnce sync.Once
	file_proto_proto_rawDescData = file_proto_proto_rawDesc
)

func file_proto_proto_rawDescGZIP() []byte {
	file_proto_proto_rawDescOnce.Do(func() {
		file_proto_proto_rawDescData = protoimpl.X.CompressGZIP(file_proto_proto_rawDescData)
	})
	return file_proto_proto_rawDescData
}

var file_proto_proto_enumTypes = make([]protoimpl.EnumInfo, 3)
var file_proto_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_proto_proto_goTypes = []interface{}{
	(Character)(0),              // 0: api.Character
	(Method)(0),                 // 1: api.Method
	(Status)(0),                 // 2: api.Status
	(*Key)(nil),                 // 3: api.Key
	(*Meta)(nil),                // 4: api.Meta
	(*Message)(nil),             // 5: api.Message
	(*Name)(nil),                // 6: api.Name
	(*Role)(nil),                // 7: api.Role
	(*Actor)(nil),               // 8: api.Actor
	(*Result)(nil),              // 9: api.Result
	(*User)(nil),                // 10: api.User
	(*timestamp.Timestamp)(nil), // 11: google.protobuf.Timestamp
	(*empty.Empty)(nil),         // 12: google.protobuf.Empty
}
var file_proto_proto_depIdxs = []int32{
	11, // 0: api.Meta.creationTime:type_name -> google.protobuf.Timestamp
	0,  // 1: api.Meta.character:type_name -> api.Character
	3,  // 2: api.Message.key:type_name -> api.Key
	4,  // 3: api.Message.meta:type_name -> api.Meta
	2,  // 4: api.Actor.status:type_name -> api.Status
	0,  // 5: api.User.character:type_name -> api.Character
	2,  // 6: api.User.status:type_name -> api.Status
	3,  // 7: api.MessageAPI.Get:input_type -> api.Key
	3,  // 8: api.MessageAPI.GetAll:input_type -> api.Key
	5,  // 9: api.MessageAPI.Put:input_type -> api.Message
	3,  // 10: api.MessageAPI.Delete:input_type -> api.Key
	3,  // 11: api.MessageAPI.DeleteAll:input_type -> api.Key
	3,  // 12: api.MessageAPI.Watch:input_type -> api.Key
	6,  // 13: api.DirectorAPI.GetActorWithName:input_type -> api.Name
	7,  // 14: api.DirectorAPI.GetActorsWithRole:input_type -> api.Role
	12, // 15: api.DirectorAPI.GetAllActors:input_type -> google.protobuf.Empty
	9,  // 16: api.DirectorAPI.PutResult:input_type -> api.Result
	6,  // 17: api.OperatorAPI.SetUserStatusUnknown:input_type -> api.Name
	6,  // 18: api.OperatorAPI.SetUserStatusRunning:input_type -> api.Name
	6,  // 19: api.OperatorAPI.SetUserStatusFailed:input_type -> api.Name
	12, // 20: api.UserAPI.ImReady:input_type -> google.protobuf.Empty
	5,  // 21: api.MessageAPI.Get:output_type -> api.Message
	5,  // 22: api.MessageAPI.GetAll:output_type -> api.Message
	12, // 23: api.MessageAPI.Put:output_type -> google.protobuf.Empty
	12, // 24: api.MessageAPI.Delete:output_type -> google.protobuf.Empty
	12, // 25: api.MessageAPI.DeleteAll:output_type -> google.protobuf.Empty
	5,  // 26: api.MessageAPI.Watch:output_type -> api.Message
	8,  // 27: api.DirectorAPI.GetActorWithName:output_type -> api.Actor
	8,  // 28: api.DirectorAPI.GetActorsWithRole:output_type -> api.Actor
	8,  // 29: api.DirectorAPI.GetAllActors:output_type -> api.Actor
	12, // 30: api.DirectorAPI.PutResult:output_type -> google.protobuf.Empty
	12, // 31: api.OperatorAPI.SetUserStatusUnknown:output_type -> google.protobuf.Empty
	12, // 32: api.OperatorAPI.SetUserStatusRunning:output_type -> google.protobuf.Empty
	12, // 33: api.OperatorAPI.SetUserStatusFailed:output_type -> google.protobuf.Empty
	12, // 34: api.UserAPI.ImReady:output_type -> google.protobuf.Empty
	21, // [21:35] is the sub-list for method output_type
	7,  // [7:21] is the sub-list for method input_type
	7,  // [7:7] is the sub-list for extension type_name
	7,  // [7:7] is the sub-list for extension extendee
	0,  // [0:7] is the sub-list for field type_name
}

func init() { file_proto_proto_init() }
func file_proto_proto_init() {
	if File_proto_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_proto_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Key); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Meta); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Message); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Name); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Role); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Actor); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Result); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*User); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_proto_proto_rawDesc,
			NumEnums:      3,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   4,
		},
		GoTypes:           file_proto_proto_goTypes,
		DependencyIndexes: file_proto_proto_depIdxs,
		EnumInfos:         file_proto_proto_enumTypes,
		MessageInfos:      file_proto_proto_msgTypes,
	}.Build()
	File_proto_proto = out.File
	file_proto_proto_rawDesc = nil
	file_proto_proto_goTypes = nil
	file_proto_proto_depIdxs = nil
}
