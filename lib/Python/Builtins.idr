module Python.Builtins

import Python
import Python.IO
import Python.RTS

%default total
%access abstract

Show_sig : Signature
Show_sig f = case f of
  "__str__" => [] ~> String
  _ => NotField

Arith_sig : Type -> Signature
Arith_sig a f = case f of
  "__add__" => [a] ~> a
  "__sub__" => [a] ~> a
  "__mul__" => [a] ~> a
  "__div__" => [a] ~> a
  _ => Show_sig f

Int_sig : Signature
Int_sig = Arith_sig Int <+> Object_sig

instance Object Int Int_sig where {}

Float_sig : Signature
Float_sig = Arith_sig Float <+> Object_sig

instance Object Float Float_sig where {}

Bool_sig : Signature
Bool_sig = Arith_sig Bool <+> Object_sig

instance Object Bool Bool_sig where {}

Str_sig : Signature
Str_sig = Object_sig

instance Object String Str_sig where {}

data Bytes : Type where {}

Bytes_sig : Signature
Bytes_sig = Object_sig

instance Object Bytes Bytes_sig where {}

data Dict : Type -> Type -> type where {}

Dict_sig : Type -> Type -> Signature
Dict_sig k v f = case f of
    "__get__" => [k] ~> v
    _ => Object_sig f

instance Object (Dict k v) (Dict_sig k v) where {}

data PyList : Type -> Type where {}

PyList_sig : Type -> Signature
PyList_sig a = Object_sig

instance Object (PyList a) (PyList_sig a) where {}

data Tuple : Type where {}

Tuple_sig : Signature
Tuple_sig = Object_sig

instance Object Tuple Tuple_sig where {}

data Set : Type -> Type where {}

Set_sig : Type -> Signature
Set_sig a = Object_sig

instance Object (Set a) (Set_sig a) where {}

data Builtins : Type where {}

Builtins_sig : Signature
Builtins_sig f = case f of
  "int"   => Attr $ PyType Int
  "float" => Attr $ PyType Float
  "bool"  => Attr $ PyType Bool
  "str"   => Attr $ PyType String
  _ => Module_sig f

instance Object Builtins Builtins_sig where {}

import_ : PIO Builtins
import_ = importModule "__builtins__"

builtins : Builtins
builtins = unsafePerformIO import_  -- __builtins__ are always safe

{-
  "list"  => attr $ PyType PyList
  "dict"  => attr $ PyType PyDict
  "set"   => attr $ PyType PySet
  "tuple" => attr $ PyType PyTuple

abstract
toPyList : List a -> Ref PyList
toPyList xs = unsafePerformIO $ list $. [toDyn xs]
-}
