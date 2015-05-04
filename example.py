#!/usr/bin/env python

import sys

Unit = '()'  # the unit constructor compiles to this

class IdrisError(Exception):
  pass

def idris_error(msg):
  raise IdrisError(msg)

MODULES = dict()

def idris_pymodule(name):
  mod = MODULES.get(name)
  if mod is None:
    mod = __import__(name)
    MODULES[name] = mod
  return mod

def idris_call(f, args):
  return f(*list(args))

def idris_foreach(it, st, f):
  for x in it:
    # Apply st, x, world
    st = APPLY0(APPLY0(APPLY0(f, st), x), None)
  return st

def idris_is_none(x):
  return 1 if x is None else 0

def idris_try(f, fail, succ):
  try:
    result = APPLY0(f, None)  # apply to world
    return APPLY0(succ, result)
  except Exception as e:
    return APPLY0(APPLY0(fail, e.__class__.__name__), e)

def idris_raise(e):
  raise e

def idris_marshal_PIO(action):
  return lambda: APPLY0(action, None)  # delayed apply-to-world

class ConsIter(object):
  def __init__(self, node):
    self.node = node

  def next(self):
    if self.node.isNil:
      raise StopIteration
    else:
      result = self.node.head
      self.node = self.node.tail
      return result

class ConsList(object):
  def __init__(self, isNil=True, head=None, tail=None):
    self.isNil = isNil
    self.head  = head
    self.tail  = tail

  def __nonzero__(self):
    return not self.isNil

  def __len__(self):
    cnt = 0
    while not self.isNil:
      self = self.tail
      cnt += 1
    return cnt

  def cons(self, x):
    return ConsList(isNil=False, head=x, tail=self)

  def __iter__(self):
    return ConsIter(self)

# Python.$.
def idris_Python_46__36__46_(e0, e1, e2, e3, e4):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      (65734, None),  # {U_Python.FFI.unRaw1}
      (65765, e3, e2, e4)  # {U_Python.{$.0}1}
    )

# Python.$:
def idris_Python_46__36__58_(e0, e1, e2, e3, e4):
  while True:
    return (65770, None, None, None, e3, (65766, e2, e4))  # {U_io_bind1}, {U_Python.{$:0}1}

# Prelude.Basics..
def idris_Prelude_46_Basics_46__46_(e0, e1, e2, e3, e4, idris_x):
  while True:
    return APPLY0(e3, APPLY0(e4, idris_x))

# Python./.
def idris_Python_46__47__46_(e0, e1, e2, e3, e4):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      (65734, None),  # {U_Python.FFI.unRaw1}
      (65767, e2, e3)  # {U_Python.{/.0}1}
    )

# Python./:
def idris_Python_46__47__58_(e0, e1, e2, e3, e4):
  while True:
    return (65770, None, None, None, e2, (65768, e3))  # {U_io_bind1}, {U_Python.{/:0}1}

# Prelude.Algebra.<+>
def idris_Prelude_46_Algebra_46__60__43__62_(e0, e1):
  while True:
    return e1

# Python.>:
def idris_Python_46__62__58_(e0, e1, e2, e3):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      (65764, None, None, None),  # {U_Python.mixout1}
      e1
    )

# Prelude.Monad.>>=
def idris_Prelude_46_Monad_46__62__62__61_(e0, e1, e2, e3):
  while True:
    if e3[0] == 0:  # constructor of Prelude.Monad.Monad
      in0, in1, = e3[1:]
      aux1 = APPLY0(APPLY0(in1, e1), e2)
    return aux1

# @@constructor of Prelude.Algebra.Monoid#Semigroup a
def idris__64__64_constructor_32_of_32_Prelude_46_Algebra_46_Monoid_35_Semigroup_32_a(
  e0, e1
):
  while True:
    if e1[0] == 0:  # constructor of Prelude.Algebra.Monoid
      in0, in1, = e1[1:]
      aux1 = in0
    return aux1

# @@constructor of Prelude.Monad.Monad#Applicative m
def idris__64__64_constructor_32_of_32_Prelude_46_Monad_46_Monad_35_Applicative_32_m(
  e0, e1
):
  while True:
    if e1[0] == 0:  # constructor of Prelude.Monad.Monad
      in0, in1, = e1[1:]
      aux1 = in0
    return aux1

# call__IO
def idris_call_95__95_IO(e0, e1, e2):
  while True:
    return APPLY0(e2, None)

# Python.Exceptions.catch
def idris_Python_46_Exceptions_46_catch(e0, e1, e2):
  while True:
    return (65770, None, None, None, e1, (65727, e2))  # {U_io_bind1}, {U_Python.Exceptions.{catch6}1}

# Python.Prim.collect
def idris_Python_46_Prim_46_collect(e0, e1):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      (65716, None, ConsList()),  # {U_Prelude.List.reverse, reverse'1}
      idris_Python_46_Prim_46_foreach(None, None, e1, ConsList(), (65746,))  # {U_Python.Prim.{collect1}1}
    )

# Prelude.Foldable.concat
def idris_Prelude_46_Foldable_46_concat(e0, e1, e2, e3):
  while True:
    if e3[0] == 0:  # constructor of Prelude.Algebra.Monoid
      in0, in1, = e3[1:]
      aux1 = in0
    if e3[0] == 0:  # constructor of Prelude.Algebra.Monoid
      in2, in3, = e3[1:]
      aux2 = in3
    return APPLY0(
      APPLY0(idris_Prelude_46_Foldable_46_foldr(None, None, None, e2), aux1),
      aux2
    )

# Prelude.Foldable.foldr
def idris_Prelude_46_Foldable_46_foldr(e0, e1, e2, e3):
  while True:
    return APPLY0(APPLY0(e3, e1), e2)

# Python.Prim.foreach
def idris_Python_46_Prim_46_foreach(e0, e1, e2, e3, e4):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__36__58_(
        None,
        None,
        (0,),  # Python.Telescope.Empty
        idris_Python_46__47__46_(None, None, e2, "__iter__", None),
        Unit
      ),
      (65748, e2, e3, e4)  # {U_Python.Prim.{foreach1}1}
    )

# Python.Lib.Threading.forkPIO
def idris_Python_46_Lib_46_Threading_46_forkPIO(e0, e1):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__36__58_(
        None,
        None,
        (1, (2,), (65736,)),  # Python.Telescope.Bind, Python.Telescope.Forall, {U_Python.Lib.Threading.{forkPIO1}1}
        idris_Python_46__47__58_(
          None,
          None,
          idris_Python_46_Lib_46_Queue_46_import_95_(),
          "Queue",
          None
        ),
        (0, (0,), (0, 1, Unit))  # Builtins.MkSigma, Data.Erased.Erase, Builtins.MkSigma
      ),
      (65741, e1)  # {U_Python.Lib.Threading.{forkPIO6}1}
    )

# Python.importModule
def idris_Python_46_importModule(e0, e1, idris_w):
  while True:
    return idris_pymodule(e1)

# Python.Lib.BeautifulSoup.import_
def idris_Python_46_Lib_46_BeautifulSoup_46_import_95_():
  while True:
    return (65763, None, "bs4")  # {U_Python.importModule1}

# Python.Lib.Os.import_
def idris_Python_46_Lib_46_Os_46_import_95_():
  while True:
    return (65763, None, "os")  # {U_Python.importModule1}

# Python.Lib.Queue.import_
def idris_Python_46_Lib_46_Queue_46_import_95_():
  while True:
    return (65763, None, "Queue")  # {U_Python.importModule1}

# Python.Lib.Requests.import_
def idris_Python_46_Lib_46_Requests_46_import_95_():
  while True:
    return (65763, None, "requests")  # {U_Python.importModule1}

# Python.Lib.Threading.import_
def idris_Python_46_Lib_46_Threading_46_import_95_():
  while True:
    return (65763, None, "threading")  # {U_Python.importModule1}

# io_bind
def idris_io_95_bind(e0, e1, e2, e3, e4, idris_w):
  while True:
    return APPLY0(io_bind2(e0, e1, e2, e3, e4, idris_w), APPLY0(e3, idris_w))

# io_return
def idris_io_95_return(e0, e1, e2, idris_w):
  while True:
    return e2

# Python.Prim.iterate
def idris_Python_46_Prim_46_iterate(e0, e1, e2, e3, e4):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__36__58_(
        None,
        None,
        (0,),  # Python.Telescope.Empty
        idris_Python_46__47__46_(None, None, e2, "__iter__", None),
        Unit
      ),
      (65749, e3, e4)  # {U_Python.Prim.{iterate0}1}
    )

# Prelude.Strings.length
def idris_Prelude_46_Strings_46_length():
  while True:
    return (
      65713,  # {U_Prelude.Basics..1}
      None,
      None,
      None,
      (65713, None, None, None, (65717,), (65772,)),  # {U_Prelude.Basics..1}, {U_Prelude.Strings.{length0}1}, {U_prim__zextInt_BigInt1}
      (65773,)  # {U_prim_lenString1}
    )

# Main.main
def idris_Main_46_main():
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Lib_46_Requests_46_import_95_(),
      (65708,)  # {U_Main.{main69}1}
    )

# Python.marshalPIO
def idris_Python_46_marshalPIO(e0, e1):
  while True:
    return idris_unsafePerformIO(None, None, (65769, e1))  # {U_Python.{marshalPIO0}1}

# Python.mixout
def idris_Python_46_mixout(e0, e1, e2, e3):
  while True:
    return e3

# mkForeignPrim
def idris_mkForeignPrim():
  while True:
    return None

# Prelude.Algebra.neutral
def idris_Prelude_46_Algebra_46_neutral(e0, e1):
  while True:
    if e1[0] == 0:  # constructor of Prelude.Algebra.Monoid
      in0, in1, = e1[1:]
      aux1 = in1
    return aux1

# Python.Prim.next
def idris_Python_46_Prim_46_next(e0, e1):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Exceptions_46_try(
        None,
        idris_Python_46__36__58_(
          None,
          None,
          (0,),  # Python.Telescope.Empty
          idris_Python_46__47__46_(None, None, e1, "next", None),
          Unit
        )
      ),
      (65753,)  # {U_Python.Prim.{next12}1}
    )

# prim__addInt
def idris_prim_95__95_addInt(op0, op1):
  while True:
    return op0 + op1

# prim__concat
def idris_prim_95__95_concat(op0, op1):
  while True:
    return op0 + op1

# prim__null
def idris_prim_95__95_null():
  while True:
    return None

# prim__readFile
def idris_prim_95__95_readFile(op0, op1):
  while True:
    return idris_error("unimplemented external: prim__readFile")

# prim__registerPtr
def idris_prim_95__95_registerPtr(op0, op1):
  while True:
    return idris_error("unimplemented external: prim__registerPtr")

# prim__stderr
def idris_prim_95__95_stderr():
  while True:
    return idris_error("unimplemented external: prim__stderr")

# prim__stdin
def idris_prim_95__95_stdin():
  while True:
    return idris_error("unimplemented external: prim__stdin")

# prim__stdout
def idris_prim_95__95_stdout():
  while True:
    return idris_error("unimplemented external: prim__stdout")

# prim__toStrBigInt
def idris_prim_95__95_toStrBigInt(op0):
  while True:
    return str(op0)

# prim__toStrInt
def idris_prim_95__95_toStrInt(op0):
  while True:
    return str(op0)

# prim__vm
def idris_prim_95__95_vm():
  while True:
    return idris_error("unimplemented external: prim__vm")

# prim__writeFile
def idris_prim_95__95_writeFile(op0, op1, op2):
  while True:
    return idris_error("unimplemented external: prim__writeFile")

# prim__writeString
def idris_prim_95__95_writeString(op0, op1):
  while True:
    return sys.stdout.write(op1)

# prim__zextInt_BigInt
def idris_prim_95__95_zextInt_95_BigInt(op0):
  while True:
    return op0

# prim_io_bind
def idris_prim_95_io_95_bind(e0, e1, e2, e3):
  while True:
    return APPLY0(e3, e2)

# prim_lenString
def idris_prim_95_lenString(op0):
  while True:
    return len(op0)

# Prelude.Applicative.pure
def idris_Prelude_46_Applicative_46_pure(e0, e1, e2):
  while True:
    return APPLY0(e2, e1)

# Prelude.putStr
def idris_Prelude_46_putStr(e0, e1):
  while True:
    return (65770, None, None, None, (65718, e1), (65719,))  # {U_io_bind1}, {U_Prelude.{putStr0}1}, {U_Prelude.{putStr1}1}

# Python.Exceptions.raise
def idris_Python_46_Exceptions_46_raise(e0, e1):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      (65734, None),  # {U_Python.FFI.unRaw1}
      (65728, e1)  # {U_Python.Exceptions.{raise0}1}
    )

# run__IO
def idris_run_95__95_IO(e0, e1):
  while True:
    return APPLY0(e1, None)

# Python.Exceptions.showException
def idris_Python_46_Exceptions_46_showException(e0):
  while True:
    return idris_unsafePerformIO(None, None, (65729, e0))  # {U_Python.Exceptions.{showException0}1}

# Python.Telescope.strip
def idris_Python_46_Telescope_46_strip(e0, e1, e2):
  while True:
    if e1[0] == 1:  # Python.Telescope.Bind
      in0, in1, = e1[1:]
      if in0[0] == 2:  # Python.Telescope.Forall
        if e2[0] == 0:  # Builtins.MkSigma
          in2, in3, = e2[1:]
          aux3 = idris_Python_46_Telescope_46_strip(None, APPLY0(in1, in2), in3)
        aux2 = aux3
      elif in0[0] == 1:  # Python.Telescope.Optional
        if e2[0] == 0:  # Builtins.MkSigma
          in4, in5, = e2[1:]
          if in4 is not None:  # Prelude.Maybe.Just
            in6 = in4
            aux5 = idris_Python_46_Telescope_46_strip(None, APPLY0(in1, in6), in5).cons(in6)
          elif in4 is None:  # Prelude.Maybe.Nothing
            aux5 = idris_Python_46_Telescope_46_strip(None, APPLY0(in1, None), in5).cons(None)
          aux4 = aux5
        aux2 = aux4
      elif in0[0] == 0:  # Python.Telescope.Pi
        if e2[0] == 0:  # Builtins.MkSigma
          in7, in8, = e2[1:]
          aux6 = idris_Python_46_Telescope_46_strip(None, APPLY0(in1, in7), in8).cons(in7)
        aux2 = aux6
      aux1 = aux2
    elif e1[0] == 0:  # Python.Telescope.Empty
      aux1 = ConsList()
    return aux1

# Python.Exceptions.try
def idris_Python_46_Exceptions_46_try(e0, e1):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      (65734, None),  # {U_Python.FFI.unRaw1}
      (65733, e1)  # {U_Python.Exceptions.{try3}1}
    )

# Python.FFI.unRaw
def idris_Python_46_FFI_46_unRaw(e0, e1):
  while True:
    return e1

# unsafePerformIO
def idris_unsafePerformIO(e0, e1, e2):
  while True:
    return APPLY0(unsafePerformIO1(e0, e1, e2), APPLY0(e2, None))

# unsafePerformPrimIO
def idris_unsafePerformPrimIO():
  while True:
    return None

# Python.Lib.Threading.wait
def idris_Python_46_Lib_46_Threading_46_wait(e0, e1):
  while True:
    return idris_Python_46__36__58_(
      None,
      None,
      (1, (0,), (65742,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{wait0}1}
      idris_Python_46__47__46_(None, None, e1, "get", None),
      (0, 1, Unit)  # Builtins.MkSigma
    )

# world
def idris_world(e0):
  while True:
    return e0

# Python.{$.0}
def idris_Python_46__123__36__46_0_125_(e3, e2, e4, in0):
  while True:
    return idris_call(e3, idris_Python_46_Telescope_46_strip(None, e2, e4))

# Python.{$:0}
def idris_Python_46__123__36__58_0_125_(e2, e4, in0):
  while True:
    return idris_Python_46__36__46_(None, None, e2, in0, e4)

# Python.{/.0}
def idris_Python_46__123__47__46_0_125_(e2, e3, in0):
  while True:
    return getattr(e2, e3)

# Python.{/:0}
def idris_Python_46__123__47__58_0_125_(e3, in0):
  while True:
    return idris_Python_46__47__46_(None, None, in0, e3, None)

# {APPLY0}
def APPLY0(fn0, arg0):
  while True:
    if fn0[0] < 65718:
      if fn0[0] < 65678:
        if fn0[0] < 65658:
          if fn0[0] < 65648:
            if fn0[0] < 65643:
              if fn0[0] < 65641:
                if fn0[0] == 65639:  # {U_Main.{case block in main_lam0}1}
                  aux1 = idris_Main_46__123_case_32_block_32_in_32_main_95_lam0_125_(arg0)
                elif fn0[0] == 65640:  # {U_Main.{case block in main_lam1}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Main_46__123_case_32_block_32_in_32_main_95_lam1_125_(P_c0, P_c1, arg0)
              else:
                if fn0[0] == 65641:  # {U_Main.{case block in main_lam2}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Main_46__123_case_32_block_32_in_32_main_95_lam2_125_(P_c0, P_c1, arg0)
                elif fn0[0] == 65642:  # {U_Main.{case block in main_lam3}1}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = idris_Main_46__123_case_32_block_32_in_32_main_95_lam3_125_(
                    P_c0, P_c1, P_c2, arg0
                  )
            else:
              if fn0[0] < 65645:
                if fn0[0] == 65643:  # {U_Main.{main0}1}
                  aux1 = idris_Main_46__123_main0_125_(arg0)
                elif fn0[0] == 65644:  # {U_Main.{main10}1}
                  aux1 = idris_Main_46__123_main10_125_(arg0)
              else:
                if fn0[0] == 65645:  # {U_Main.{main11}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main11_125_(P_c0, arg0)
                elif fn0[0] == 65646:  # {U_Main.{main12}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main12_125_(P_c0, arg0)
                elif fn0[0] == 65647:  # {U_Main.{main13}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main13_125_(P_c0, arg0)
          else:
            if fn0[0] < 65653:
              if fn0[0] < 65650:
                if fn0[0] == 65648:  # {U_Main.{main14}1}
                  aux1 = idris_Main_46__123_main14_125_(arg0)
                elif fn0[0] == 65649:  # {U_Main.{main15}1}
                  aux1 = idris_Main_46__123_main15_125_(arg0)
              else:
                if fn0[0] == 65650:  # {U_Main.{main16}1}
                  aux1 = idris_Main_46__123_main16_125_(arg0)
                elif fn0[0] == 65651:  # {U_Main.{main17}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main17_125_(P_c0, arg0)
                elif fn0[0] == 65652:  # {U_Main.{main18}1}
                  aux1 = idris_Main_46__123_main18_125_(arg0)
            else:
              if fn0[0] < 65655:
                if fn0[0] == 65653:  # {U_Main.{main19}1}
                  aux1 = idris_Main_46__123_main19_125_(arg0)
                elif fn0[0] == 65654:  # {U_Main.{main1}1}
                  aux1 = idris_Main_46__123_main1_125_(arg0)
              else:
                if fn0[0] == 65655:  # {U_Main.{main20}1}
                  aux1 = idris_Main_46__123_main20_125_(arg0)
                elif fn0[0] == 65656:  # {U_Main.{main21}1}
                  aux1 = idris_Main_46__123_main21_125_(arg0)
                elif fn0[0] == 65657:  # {U_Main.{main22}1}
                  aux1 = idris_Main_46__123_main22_125_(arg0)
        else:
          if fn0[0] < 65668:
            if fn0[0] < 65663:
              if fn0[0] < 65660:
                if fn0[0] == 65658:  # {U_Main.{main23}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main23_125_(P_c0, arg0)
                elif fn0[0] == 65659:  # {U_Main.{main24}1}
                  aux1 = idris_Main_46__123_main24_125_(arg0)
              else:
                if fn0[0] == 65660:  # {U_Main.{main25}1}
                  aux1 = idris_Main_46__123_main25_125_(arg0)
                elif fn0[0] == 65661:  # {U_Main.{main26}1}
                  aux1 = idris_Main_46__123_main26_125_(arg0)
                elif fn0[0] == 65662:  # {U_Main.{main27}1}
                  aux1 = idris_Main_46__123_main27_125_(arg0)
            else:
              if fn0[0] < 65665:
                if fn0[0] == 65663:  # {U_Main.{main28}1}
                  aux1 = idris_Main_46__123_main28_125_(arg0)
                elif fn0[0] == 65664:  # {U_Main.{main29}1}
                  aux1 = idris_Main_46__123_main29_125_(arg0)
              else:
                if fn0[0] == 65665:  # {U_Main.{main2}1}
                  aux1 = idris_Main_46__123_main2_125_(arg0)
                elif fn0[0] == 65666:  # {U_Main.{main30}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main30_125_(P_c0, arg0)
                elif fn0[0] == 65667:  # {U_Main.{main31}1}
                  aux1 = idris_Main_46__123_main31_125_(arg0)
          else:
            if fn0[0] < 65673:
              if fn0[0] < 65670:
                if fn0[0] == 65668:  # {U_Main.{main32}1}
                  aux1 = idris_Main_46__123_main32_125_(arg0)
                elif fn0[0] == 65669:  # {U_Main.{main33}1}
                  aux1 = idris_Main_46__123_main33_125_(arg0)
              else:
                if fn0[0] == 65670:  # {U_Main.{main34}1}
                  aux1 = idris_Main_46__123_main34_125_(arg0)
                elif fn0[0] == 65671:  # {U_Main.{main35}1}
                  aux1 = idris_Main_46__123_main35_125_(arg0)
                elif fn0[0] == 65672:  # {U_Main.{main36}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main36_125_(P_c0, arg0)
            else:
              if fn0[0] < 65675:
                if fn0[0] == 65673:  # {U_Main.{main37}1}
                  aux1 = idris_Main_46__123_main37_125_(arg0)
                elif fn0[0] == 65674:  # {U_Main.{main38}1}
                  aux1 = idris_Main_46__123_main38_125_(arg0)
              else:
                if fn0[0] == 65675:  # {U_Main.{main39}1}
                  aux1 = idris_Main_46__123_main39_125_(arg0)
                elif fn0[0] == 65676:  # {U_Main.{main3}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Main_46__123_main3_125_(P_c0, P_c1, arg0)
                elif fn0[0] == 65677:  # {U_Main.{main40}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main40_125_(P_c0, arg0)
      else:
        if fn0[0] < 65698:
          if fn0[0] < 65688:
            if fn0[0] < 65683:
              if fn0[0] < 65680:
                if fn0[0] == 65678:  # {U_Main.{main41}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main41_125_(P_c0, arg0)
                elif fn0[0] == 65679:  # {U_Main.{main42}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Main_46__123_main42_125_(P_c0, P_c1, arg0)
              else:
                if fn0[0] == 65680:  # {U_Main.{main43}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main43_125_(P_c0, arg0)
                elif fn0[0] == 65681:  # {U_Main.{main44}1}
                  aux1 = idris_Main_46__123_main44_125_(arg0)
                elif fn0[0] == 65682:  # {U_Main.{main45}1}
                  aux1 = idris_Main_46__123_main45_125_(arg0)
            else:
              if fn0[0] < 65685:
                if fn0[0] == 65683:  # {U_Main.{main46}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main46_125_(P_c0, arg0)
                elif fn0[0] == 65684:  # {U_Main.{main47}1}
                  aux1 = idris_Main_46__123_main47_125_(arg0)
              else:
                if fn0[0] == 65685:  # {U_Main.{main48}1}
                  aux1 = idris_Main_46__123_main48_125_(arg0)
                elif fn0[0] == 65686:  # {U_Main.{main49}1}
                  aux1 = idris_Main_46__123_main49_125_(arg0)
                elif fn0[0] == 65687:  # {U_Main.{main4}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main4_125_(P_c0, arg0)
          else:
            if fn0[0] < 65693:
              if fn0[0] < 65690:
                if fn0[0] == 65688:  # {U_Main.{main50}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main50_125_(P_c0, arg0)
                elif fn0[0] == 65689:  # {U_Main.{main51}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main51_125_(P_c0, arg0)
              else:
                if fn0[0] == 65690:  # {U_Main.{main52}1}
                  aux1 = idris_Main_46__123_main52_125_(arg0)
                elif fn0[0] == 65691:  # {U_Main.{main53}1}
                  aux1 = idris_Main_46__123_main53_125_(arg0)
                elif fn0[0] == 65692:  # {U_Main.{main54}1}
                  aux1 = idris_Main_46__123_main54_125_(arg0)
            else:
              if fn0[0] < 65695:
                if fn0[0] == 65693:  # {U_Main.{main55}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main55_125_(P_c0, arg0)
                elif fn0[0] == 65694:  # {U_Main.{main56}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main56_125_(P_c0, arg0)
              else:
                if fn0[0] == 65695:  # {U_Main.{main57}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main57_125_(P_c0, arg0)
                elif fn0[0] == 65696:  # {U_Main.{main58}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main58_125_(P_c0, arg0)
                elif fn0[0] == 65697:  # {U_Main.{main59}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main59_125_(P_c0, arg0)
        else:
          if fn0[0] < 65708:
            if fn0[0] < 65703:
              if fn0[0] < 65700:
                if fn0[0] == 65698:  # {U_Main.{main5}1}
                  aux1 = idris_Main_46__123_main5_125_(arg0)
                elif fn0[0] == 65699:  # {U_Main.{main60}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main60_125_(P_c0, arg0)
              else:
                if fn0[0] == 65700:  # {U_Main.{main61}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main61_125_(P_c0, arg0)
                elif fn0[0] == 65701:  # {U_Main.{main62}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main62_125_(P_c0, arg0)
                elif fn0[0] == 65702:  # {U_Main.{main63}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Main_46__123_main63_125_(P_c0, P_c1, arg0)
            else:
              if fn0[0] < 65705:
                if fn0[0] == 65703:  # {U_Main.{main64}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main64_125_(P_c0, arg0)
                elif fn0[0] == 65704:  # {U_Main.{main65}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main65_125_(P_c0, arg0)
              else:
                if fn0[0] == 65705:  # {U_Main.{main66}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Main_46__123_main66_125_(P_c0, P_c1, arg0)
                elif fn0[0] == 65706:  # {U_Main.{main67}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main67_125_(P_c0, arg0)
                elif fn0[0] == 65707:  # {U_Main.{main68}1}
                  aux1 = idris_Main_46__123_main68_125_(arg0)
          else:
            if fn0[0] < 65713:
              if fn0[0] < 65710:
                if fn0[0] == 65708:  # {U_Main.{main69}1}
                  aux1 = idris_Main_46__123_main69_125_(arg0)
                elif fn0[0] == 65709:  # {U_Main.{main6}1}
                  aux1 = idris_Main_46__123_main6_125_(arg0)
              else:
                if fn0[0] == 65710:  # {U_Main.{main7}1}
                  aux1 = idris_Main_46__123_main7_125_(arg0)
                elif fn0[0] == 65711:  # {U_Main.{main8}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Main_46__123_main8_125_(P_c0, arg0)
                elif fn0[0] == 65712:  # {U_Main.{main9}1}
                  aux1 = idris_Main_46__123_main9_125_(arg0)
            else:
              if fn0[0] < 65715:
                if fn0[0] == 65713:  # {U_Prelude.Basics..1}
                  P_c0, P_c1, P_c2, P_c3, P_c4, = fn0[1:]
                  aux1 = idris_Prelude_46_Basics_46__46_(P_c0, P_c1, P_c2, P_c3, P_c4, arg0)
                elif fn0[0] == 65714:  # {U_Prelude.Functor.{Prelude.IO' ffi instance of Prelude.Functor.Functor, method map_lam0}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Prelude_46_Functor_46__123_Prelude_46_IO_39__32_ffi_32_instance_32_of_32_Prelude_46_Functor_46_Functor_44__32_method_32_map_95_lam0_125_(
                    P_c0, arg0
                  )
              else:
                if fn0[0] == 65715:  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable1}
                  P_c0, P_c1, P_c2, P_c3, = fn0[1:]
                  aux1 = idris_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List(
                    P_c0, P_c1, P_c2, P_c3, arg0
                  )
                elif fn0[0] == 65716:  # {U_Prelude.List.reverse, reverse'1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Prelude_46_List_46_reverse_58_reverse_39__58_0(P_c0, P_c1, arg0)
                elif fn0[0] == 65717:  # {U_Prelude.Strings.{length0}1}
                  aux1 = idris_Prelude_46_Strings_46__123_length0_125_(arg0)
    else:
      if fn0[0] < 65757:
        if fn0[0] < 65737:
          if fn0[0] < 65727:
            if fn0[0] < 65722:
              if fn0[0] < 65720:
                if fn0[0] == 65718:  # {U_Prelude.{putStr0}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Prelude_46__123_putStr0_125_(P_c0, arg0)
                elif fn0[0] == 65719:  # {U_Prelude.{putStr1}1}
                  aux1 = idris_Prelude_46__123_putStr1_125_(arg0)
              else:
                if fn0[0] == 65720:  # {U_Python.Exceptions.case block in try1}
                  P_c0, P_c1, P_c2, P_c3, P_c4, P_c5, P_c6, = fn0[1:]
                  aux1 = idris_Python_46_Exceptions_46_try_95_case(
                    P_c0, P_c1, P_c2, P_c3, P_c4, P_c5, P_c6, arg0
                  )
                elif fn0[0] == 65721:  # {U_Python.Exceptions.{catch0}1}
                  aux1 = idris_Python_46_Exceptions_46__123_catch0_125_(arg0)
            else:
              if fn0[0] < 65724:
                if fn0[0] == 65722:  # {U_Python.Exceptions.{catch1}1}
                  aux1 = idris_Python_46_Exceptions_46__123_catch1_125_(arg0)
                elif fn0[0] == 65723:  # {U_Python.Exceptions.{catch2}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Exceptions_46__123_catch2_125_(P_c0, arg0)
              else:
                if fn0[0] == 65724:  # {U_Python.Exceptions.{catch3}1}
                  aux1 = idris_Python_46_Exceptions_46__123_catch3_125_(arg0)
                elif fn0[0] == 65725:  # {U_Python.Exceptions.{catch4}1}
                  aux1 = idris_Python_46_Exceptions_46__123_catch4_125_(arg0)
                elif fn0[0] == 65726:  # {U_Python.Exceptions.{catch5}1}
                  aux1 = idris_Python_46_Exceptions_46__123_catch5_125_(arg0)
          else:
            if fn0[0] < 65732:
              if fn0[0] < 65729:
                if fn0[0] == 65727:  # {U_Python.Exceptions.{catch6}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Exceptions_46__123_catch6_125_(P_c0, arg0)
                elif fn0[0] == 65728:  # {U_Python.Exceptions.{raise0}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Exceptions_46__123_raise0_125_(P_c0, arg0)
              else:
                if fn0[0] == 65729:  # {U_Python.Exceptions.{showException0}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Exceptions_46__123_showException0_125_(P_c0, arg0)
                elif fn0[0] == 65730:  # {U_Python.Exceptions.{try0}1}
                  aux1 = idris_Python_46_Exceptions_46__123_try0_125_(arg0)
                elif fn0[0] == 65731:  # {U_Python.Exceptions.{try1}1}
                  aux1 = idris_Python_46_Exceptions_46__123_try1_125_(arg0)
            else:
              if fn0[0] < 65734:
                if fn0[0] == 65732:  # {U_Python.Exceptions.{try2}1}
                  aux1 = idris_Python_46_Exceptions_46__123_try2_125_(arg0)
                elif fn0[0] == 65733:  # {U_Python.Exceptions.{try3}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Exceptions_46__123_try3_125_(P_c0, arg0)
              else:
                if fn0[0] == 65734:  # {U_Python.FFI.unRaw1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_FFI_46_unRaw(P_c0, arg0)
                elif fn0[0] == 65735:  # {U_Python.Lib.Threading.{forkPIO0}1}
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_forkPIO0_125_(arg0)
                elif fn0[0] == 65736:  # {U_Python.Lib.Threading.{forkPIO1}1}
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_forkPIO1_125_(arg0)
        else:
          if fn0[0] < 65747:
            if fn0[0] < 65742:
              if fn0[0] < 65739:
                if fn0[0] == 65737:  # {U_Python.Lib.Threading.{forkPIO2}1}
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_forkPIO2_125_(arg0)
                elif fn0[0] == 65738:  # {U_Python.Lib.Threading.{forkPIO3}1}
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_forkPIO3_125_(arg0)
              else:
                if fn0[0] == 65739:  # {U_Python.Lib.Threading.{forkPIO4}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_forkPIO4_125_(P_c0, arg0)
                elif fn0[0] == 65740:  # {U_Python.Lib.Threading.{forkPIO5}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_forkPIO5_125_(P_c0, arg0)
                elif fn0[0] == 65741:  # {U_Python.Lib.Threading.{forkPIO6}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_forkPIO6_125_(P_c0, arg0)
            else:
              if fn0[0] < 65744:
                if fn0[0] == 65742:  # {U_Python.Lib.Threading.{wait0}1}
                  aux1 = idris_Python_46_Lib_46_Threading_46__123_wait0_125_(arg0)
                elif fn0[0] == 65743:  # {U_Python.Prim.collect1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46_collect(P_c0, arg0)
              else:
                if fn0[0] == 65744:  # {U_Python.Prim.{case block in Python.Prim.iterate, iter_lam0}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46__123_case_32_block_32_in_32_Python_46_Prim_46_iterate_44__32_iter_95_lam0_125_(
                    P_c0, P_c1, arg0
                  )
                elif fn0[0] == 65745:  # {U_Python.Prim.{collect0}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46__123_collect0_125_(P_c0, arg0)
                elif fn0[0] == 65746:  # {U_Python.Prim.{collect1}1}
                  aux1 = idris_Python_46_Prim_46__123_collect1_125_(arg0)
          else:
            if fn0[0] < 65752:
              if fn0[0] < 65749:
                if fn0[0] == 65747:  # {U_Python.Prim.{foreach0}1}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46__123_foreach0_125_(P_c0, P_c1, P_c2, arg0)
                elif fn0[0] == 65748:  # {U_Python.Prim.{foreach1}1}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46__123_foreach1_125_(P_c0, P_c1, P_c2, arg0)
              else:
                if fn0[0] == 65749:  # {U_Python.Prim.{iterate0}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46__123_iterate0_125_(P_c0, P_c1, arg0)
                elif fn0[0] == 65750:  # {U_Python.Prim.{next0}1}
                  aux1 = idris_Python_46_Prim_46__123_next0_125_(arg0)
                elif fn0[0] == 65751:  # {U_Python.Prim.{next10}1}
                  aux1 = idris_Python_46_Prim_46__123_next10_125_(arg0)
            else:
              if fn0[0] < 65754:
                if fn0[0] == 65752:  # {U_Python.Prim.{next11}1}
                  aux1 = idris_Python_46_Prim_46__123_next11_125_(arg0)
                elif fn0[0] == 65753:  # {U_Python.Prim.{next12}1}
                  aux1 = idris_Python_46_Prim_46__123_next12_125_(arg0)
              else:
                if fn0[0] == 65754:  # {U_Python.Prim.{next1}1}
                  aux1 = idris_Python_46_Prim_46__123_next1_125_(arg0)
                elif fn0[0] == 65755:  # {U_Python.Prim.{next2}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46__123_next2_125_(P_c0, arg0)
                elif fn0[0] == 65756:  # {U_Python.Prim.{next3}1}
                  aux1 = idris_Python_46_Prim_46__123_next3_125_(arg0)
      else:
        if fn0[0] < 65777:
          if fn0[0] < 65767:
            if fn0[0] < 65762:
              if fn0[0] < 65759:
                if fn0[0] == 65757:  # {U_Python.Prim.{next4}1}
                  aux1 = idris_Python_46_Prim_46__123_next4_125_(arg0)
                elif fn0[0] == 65758:  # {U_Python.Prim.{next5}1}
                  aux1 = idris_Python_46_Prim_46__123_next5_125_(arg0)
              else:
                if fn0[0] == 65759:  # {U_Python.Prim.{next6}1}
                  aux1 = idris_Python_46_Prim_46__123_next6_125_(arg0)
                elif fn0[0] == 65760:  # {U_Python.Prim.{next7}1}
                  aux1 = idris_Python_46_Prim_46__123_next7_125_(arg0)
                elif fn0[0] == 65761:  # {U_Python.Prim.{next8}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46_Prim_46__123_next8_125_(P_c0, arg0)
            else:
              if fn0[0] < 65764:
                if fn0[0] == 65762:  # {U_Python.Prim.{next9}1}
                  aux1 = idris_Python_46_Prim_46__123_next9_125_(arg0)
                elif fn0[0] == 65763:  # {U_Python.importModule1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Python_46_importModule(P_c0, P_c1, arg0)
              else:
                if fn0[0] == 65764:  # {U_Python.mixout1}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = idris_Python_46_mixout(P_c0, P_c1, P_c2, arg0)
                elif fn0[0] == 65765:  # {U_Python.{$.0}1}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = idris_Python_46__123__36__46_0_125_(P_c0, P_c1, P_c2, arg0)
                elif fn0[0] == 65766:  # {U_Python.{$:0}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Python_46__123__36__58_0_125_(P_c0, P_c1, arg0)
          else:
            if fn0[0] < 65772:
              if fn0[0] < 65769:
                if fn0[0] == 65767:  # {U_Python.{/.0}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris_Python_46__123__47__46_0_125_(P_c0, P_c1, arg0)
                elif fn0[0] == 65768:  # {U_Python.{/:0}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46__123__47__58_0_125_(P_c0, arg0)
              else:
                if fn0[0] == 65769:  # {U_Python.{marshalPIO0}1}
                  P_c0, = fn0[1:]
                  aux1 = idris_Python_46__123_marshalPIO0_125_(P_c0, arg0)
                elif fn0[0] == 65770:  # {U_io_bind1}
                  P_c0, P_c1, P_c2, P_c3, P_c4, = fn0[1:]
                  aux1 = idris_io_95_bind(P_c0, P_c1, P_c2, P_c3, P_c4, arg0)
                elif fn0[0] == 65771:  # {U_io_return1}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = idris_io_95_return(P_c0, P_c1, P_c2, arg0)
            else:
              if fn0[0] < 65774:
                if fn0[0] == 65772:  # {U_prim__zextInt_BigInt1}
                  aux1 = idris_prim_95__95_zextInt_95_BigInt(arg0)
                elif fn0[0] == 65773:  # {U_prim_lenString1}
                  aux1 = idris_prim_95_lenString(arg0)
              else:
                if fn0[0] == 65774:  # {U_{Python.Lib.Threading.forkPIO, worker_lam0}1}
                  aux1 = idris__123_Python_46_Lib_46_Threading_46_forkPIO_44__32_worker_95_lam0_125_(
                    arg0
                  )
                elif fn0[0] == 65775:  # {U_{Python.Lib.Threading.forkPIO, worker_lam1}1}
                  P_c0, = fn0[1:]
                  aux1 = idris__123_Python_46_Lib_46_Threading_46_forkPIO_44__32_worker_95_lam1_125_(
                    P_c0, arg0
                  )
                elif fn0[0] == 65776:  # {U_{Python.Prim.iterate, iter_lam0}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam0_125_(arg0)
        else:
          if fn0[0] < 65787:
            if fn0[0] < 65782:
              if fn0[0] < 65779:
                if fn0[0] == 65777:  # {U_{Python.Prim.iterate, iter_lam10}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam10_125_(arg0)
                elif fn0[0] == 65778:  # {U_{Python.Prim.iterate, iter_lam11}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam11_125_(arg0)
              else:
                if fn0[0] == 65779:  # {U_{Python.Prim.iterate, iter_lam12}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam12_125_(arg0)
                elif fn0[0] == 65780:  # {U_{Python.Prim.iterate, iter_lam13}1}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam13_125_(
                    P_c0, P_c1, P_c2, arg0
                  )
                elif fn0[0] == 65781:  # {U_{Python.Prim.iterate, iter_lam1}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam1_125_(arg0)
            else:
              if fn0[0] < 65784:
                if fn0[0] == 65782:  # {U_{Python.Prim.iterate, iter_lam2}1}
                  P_c0, = fn0[1:]
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam2_125_(P_c0, arg0)
                elif fn0[0] == 65783:  # {U_{Python.Prim.iterate, iter_lam3}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam3_125_(arg0)
              else:
                if fn0[0] == 65784:  # {U_{Python.Prim.iterate, iter_lam4}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam4_125_(arg0)
                elif fn0[0] == 65785:  # {U_{Python.Prim.iterate, iter_lam5}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam5_125_(arg0)
                elif fn0[0] == 65786:  # {U_{Python.Prim.iterate, iter_lam6}1}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam6_125_(P_c0, P_c1, arg0)
          else:
            if fn0[0] < 65792:
              if fn0[0] < 65789:
                if fn0[0] == 65787:  # {U_{Python.Prim.iterate, iter_lam7}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam7_125_(arg0)
                elif fn0[0] == 65788:  # {U_{Python.Prim.iterate, iter_lam8}1}
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam8_125_(arg0)
              else:
                if fn0[0] == 65789:  # {U_{Python.Prim.iterate, iter_lam9}1}
                  P_c0, = fn0[1:]
                  aux1 = idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam9_125_(P_c0, arg0)
                elif fn0[0] == 65790:  # {U_{io_bind1}1}
                  P_c0, P_c1, P_c2, P_c3, P_c4, P_c5, = fn0[1:]
                  aux1 = io_bind1(P_c0, P_c1, P_c2, P_c3, P_c4, P_c5, arg0)
                elif fn0[0] == 65791:  # {U_{unsafePerformIO0}1}
                  aux1 = unsafePerformIO0(arg0)
            else:
              if fn0[0] < 65794:
                if fn0[0] == 65792:  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable2}
                  P_c0, P_c1, P_c2, = fn0[1:]
                  aux1 = (65715, P_c0, P_c1, P_c2, arg0)  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable1}
                elif fn0[0] == 65793:  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable3}
                  P_c0, P_c1, = fn0[1:]
                  aux1 = (65792, P_c0, P_c1, arg0)  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable2}
              else:
                if fn0[0] == 65794:  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable4}
                  P_c0, = fn0[1:]
                  aux1 = (65793, P_c0, arg0)  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable3}
                elif fn0[0] == 65795:  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable5}
                  aux1 = (65794, arg0)  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable4}
    return aux1

# {EVAL0}
def EVAL0(arg0):
  while True:
    return arg0

# Prelude.Functor.{Prelude.IO' ffi instance of Prelude.Functor.Functor, method map_lam0}
def idris_Prelude_46_Functor_46__123_Prelude_46_IO_39__32_ffi_32_instance_32_of_32_Prelude_46_Functor_46_Functor_44__32_method_32_map_95_lam0_125_(
  e3, in0
):
  while True:
    return (65771, None, None, APPLY0(e3, in0))  # {U_io_return1}

# {Python.Lib.Threading.forkPIO, worker_lam0}
def idris__123_Python_46_Lib_46_Threading_46_forkPIO_44__32_worker_95_lam0_125_(in1):
  while True:
    return (0,)  # Python.Telescope.Empty

# {Python.Prim.iterate, iter_lam0}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam0_125_(in2):
  while True:
    return (65771, None, None, in2)  # {U_io_return1}

# Python.Prim.{case block in Python.Prim.iterate, iter_lam0}
def idris_Python_46_Prim_46__123_case_32_block_32_in_32_Python_46_Prim_46_iterate_44__32_iter_95_lam0_125_(
  e6, e9, in1
):
  while True:
    return idris_Python_46_Prim_46_iterate_58_iter_58_0(
      None, None, None, None, None, None, None, e6, in1, e9
    )

# Main.{case block in main_lam0}
def idris_Main_46__123_case_32_block_32_in_32_main_95_lam0_125_(in1):
  while True:
    return (0,)  # Python.Telescope.Empty

# Python.Exceptions.{catch0}
def idris_Python_46_Exceptions_46__123_catch0_125_(in2):
  while True:
    return (65771, None, None, in2)  # {U_io_return1}

# Python.Prim.{collect0}
def idris_Python_46_Prim_46__123_collect0_125_(in0, in1):
  while True:
    return (65771, None, None, in0.cons(in1))  # {U_io_return1}

# Python.Prim.{foreach0}
def idris_Python_46_Prim_46__123_foreach0_125_(e2, e3, e4, in1):
  while True:
    return idris_foreach(e2, e3, e4)

# Python.Lib.Threading.{forkPIO0}
def idris_Python_46_Lib_46_Threading_46__123_forkPIO0_125_(in1):
  while True:
    return (0,)  # Python.Telescope.Empty

# {io_bind0}
def io_bind0(e0, e1, e2, e3, e4, idris_w, in0):
  while True:
    return APPLY0(e4, in0)

# Python.Prim.{iterate0}
def idris_Python_46_Prim_46__123_iterate0_125_(e3, e4, in0):
  while True:
    return idris_Python_46_Prim_46_iterate_58_iter_58_0(
      None, None, None, None, None, None, None, in0, e3, e4
    )

# Prelude.Strings.{length0}
def idris_Prelude_46_Strings_46__123_length0_125_(in0):
  while True:
    return in0

# Main.{main0}
def idris_Main_46__123_main0_125_(in2):
  while True:
    return (0,)  # Python.Telescope.Empty

# Python.{marshalPIO0}
def idris_Python_46__123_marshalPIO0_125_(e1, in0):
  while True:
    return idris_marshal_PIO(e1)

# Python.Prim.{next0}
def idris_Python_46_Prim_46__123_next0_125_(in2):
  while True:
    return (65771, None, None, in2)  # {U_io_return1}

# Prelude.{putStr0}
def idris_Prelude_46__123_putStr0_125_(e1, in0):
  while True:
    return sys.stdout.write(e1)

# Python.Exceptions.{raise0}
def idris_Python_46_Exceptions_46__123_raise0_125_(e1, in0):
  while True:
    return idris_raise(e1)

# {runMain0}
def runMain0():
  while True:
    return EVAL0(APPLY0(idris_Main_46_main(), None))

# Python.Exceptions.{showException0}
def idris_Python_46_Exceptions_46__123_showException0_125_(e0, in0):
  while True:
    return str(e0)

# Python.Exceptions.{try0}
def idris_Python_46_Exceptions_46__123_try0_125_(in1):
  while True:
    return (65720, None, None, None, None, None, in1, None)  # {U_Python.Exceptions.case block in try1}

# {unsafePerformIO0}
def unsafePerformIO0(in0):
  while True:
    return in0

# Python.Lib.Threading.{wait0}
def idris_Python_46_Lib_46_Threading_46__123_wait0_125_(in0):
  while True:
    return (0,)  # Python.Telescope.Empty

# {Python.Lib.Threading.forkPIO, worker_lam1}
def idris__123_Python_46_Lib_46_Threading_46_forkPIO_44__32_worker_95_lam1_125_(
  e2, in0
):
  while True:
    return idris_Python_46__36__58_(
      None,
      None,
      (1, (0,), (65774,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_{Python.Lib.Threading.forkPIO, worker_lam0}1}
      idris_Python_46__47__46_(None, None, e2, "put", None),
      (0, in0, Unit)  # Builtins.MkSigma
    )

# {Python.Prim.iterate, iter_lam1}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam1_125_(in1):
  while True:
    return (65776,)  # {U_{Python.Prim.iterate, iter_lam0}1}

# Main.{case block in main_lam1}
def idris_Main_46__123_case_32_block_32_in_32_main_95_lam1_125_(e18, in2, in3):
  while True:
    if e18[0] == 0:  # constructor of Prelude.Monad.Monad
      in4, in5, = e18[1:]
      aux1 = in4
    return APPLY0(
      idris_Prelude_46_Applicative_46_pure(None, None, aux1),
      APPLY0(idris_Prelude_46_Strings_46_length(), in2)
    )

# Python.Exceptions.{catch1}
def idris_Python_46_Exceptions_46__123_catch1_125_(in1):
  while True:
    return (65721,)  # {U_Python.Exceptions.{catch0}1}

# Python.Prim.{collect1}
def idris_Python_46_Prim_46__123_collect1_125_(in0):
  while True:
    return (65745, in0)  # {U_Python.Prim.{collect0}1}

# Python.Prim.{foreach1}
def idris_Python_46_Prim_46__123_foreach1_125_(e2, e3, e4, in0):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      (65734, None),  # {U_Python.FFI.unRaw1}
      (65747, e2, e3, e4)  # {U_Python.Prim.{foreach0}1}
    )

# Python.Lib.Threading.{forkPIO1}
def idris_Python_46_Lib_46_Threading_46__123_forkPIO1_125_(in0):
  while True:
    return (1, (1,), (65735,))  # Python.Telescope.Bind, Python.Telescope.Optional, {U_Python.Lib.Threading.{forkPIO0}1}

# {io_bind1}
def io_bind1(e0, e1, e2, e3, e4, idris_w, in0):
  while True:
    return APPLY0(io_bind0(e0, e1, e2, e3, e4, idris_w, in0), idris_w)

# Main.{main1}
def idris_Main_46__123_main1_125_(in5):
  while True:
    return (0,)  # Python.Telescope.Empty

# Python.Prim.{next1}
def idris_Python_46_Prim_46__123_next1_125_(in1):
  while True:
    return (65750,)  # {U_Python.Prim.{next0}1}

# Prelude.{putStr1}
def idris_Prelude_46__123_putStr1_125_(in1):
  while True:
    return (65771, None, None, Unit)  # {U_io_return1}

# Python.Exceptions.{try1}
def idris_Python_46_Exceptions_46__123_try1_125_(in2):
  while True:
    return in2

# {unsafePerformIO1}
def unsafePerformIO1(e0, e1, e2):
  while True:
    return (65791,)  # {U_{unsafePerformIO0}1}

# {Python.Prim.iterate, iter_lam2}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam2_125_(in5, in6):
  while True:
    return (65770, None, None, None, in5, in6)  # {U_io_bind1}

# Main.{case block in main_lam2}
def idris_Main_46__123_case_32_block_32_in_32_main_95_lam2_125_(e18, e20, in2):
  while True:
    return APPLY0(
      APPLY0(
        idris_Prelude_46_Monad_46__62__62__61_(None, None, None, e18),
        idris_Prelude_46_putStr(None, "thread " + e20 + " done" + "\n")
      ),
      (65640, e18, in2)  # {U_Main.{case block in main_lam1}1}
    )

# Python.Exceptions.{catch2}
def idris_Python_46_Exceptions_46__123_catch2_125_(in5, in6):
  while True:
    return (65770, None, None, None, in5, in6)  # {U_io_bind1}

# Python.Lib.Threading.{forkPIO2}
def idris_Python_46_Lib_46_Threading_46__123_forkPIO2_125_(in4):
  while True:
    return (0,)  # Python.Telescope.Empty

# {io_bind2}
def io_bind2(e0, e1, e2, e3, e4, idris_w):
  while True:
    return (65790, e0, e1, e2, e3, e4, idris_w)  # {U_{io_bind1}1}

# Main.{main2}
def idris_Main_46__123_main2_125_(in7):
  while True:
    return (0,)  # Python.Telescope.Empty

# Python.Prim.{next2}
def idris_Python_46_Prim_46__123_next2_125_(in5, in6):
  while True:
    return (65770, None, None, None, in5, in6)  # {U_io_bind1}

# Python.Exceptions.{try2}
def idris_Python_46_Exceptions_46__123_try2_125_(in3):
  while True:
    return (0, in3)  # Python.Exceptions.OK

# {Python.Prim.iterate, iter_lam3}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam3_125_(in5):
  while True:
    return (65782, in5)  # {U_{Python.Prim.iterate, iter_lam2}1}

# Main.{case block in main_lam3}
def idris_Main_46__123_case_32_block_32_in_32_main_95_lam3_125_(e18, e3, e20, in0):
  while True:
    return APPLY0(
      APPLY0(
        idris_Prelude_46_Monad_46__62__62__61_(None, None, None, e18),
        idris_Python_46__47__58_(
          None,
          None,
          idris_Python_46__36__58_(
            None,
            None,
            (1, (0,), (65639,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Main.{case block in main_lam0}1}
            idris_Python_46__47__46_(None, None, e3, "get", None),
            (0, "http://idris-lang.org", Unit)  # Builtins.MkSigma
          ),
          "text",
          None
        )
      ),
      (65641, e18, e20)  # {U_Main.{case block in main_lam2}1}
    )

# Python.Exceptions.{catch3}
def idris_Python_46_Exceptions_46__123_catch3_125_(in5):
  while True:
    return (65723, in5)  # {U_Python.Exceptions.{catch2}1}

# Python.Lib.Threading.{forkPIO3}
def idris_Python_46_Lib_46_Threading_46__123_forkPIO3_125_(in3):
  while True:
    return (1, (0,), (65737,))  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO2}1}

# Main.{main3}
def idris_Main_46__123_main3_125_(in15, in16, in17):
  while True:
    return idris_Prelude_46_Foldable_46_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List_58__33_foldr_58_0(
      None, None, in15, in16, in17
    )

# Python.Prim.{next3}
def idris_Python_46_Prim_46__123_next3_125_(in5):
  while True:
    return (65755, in5)  # {U_Python.Prim.{next2}1}

# Python.Exceptions.{try3}
def idris_Python_46_Exceptions_46__123_try3_125_(e1, in0):
  while True:
    return idris_try(
      e1,
      (65730,),  # {U_Python.Exceptions.{try0}1}
      (
        65713,  # {U_Prelude.Basics..1}
        None,
        None,
        None,
        (65713, None, None, None, (65731,), (65732,)),  # {U_Prelude.Basics..1}, {U_Python.Exceptions.{try1}1}, {U_Python.Exceptions.{try2}1}
        (65734, None)  # {U_Python.FFI.unRaw1}
      )
    )

# {Python.Prim.iterate, iter_lam4}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam4_125_(in4):
  while True:
    return (65783,)  # {U_{Python.Prim.iterate, iter_lam3}1}

# Python.Exceptions.{catch4}
def idris_Python_46_Exceptions_46__123_catch4_125_(in4):
  while True:
    return (65724,)  # {U_Python.Exceptions.{catch3}1}

# Python.Lib.Threading.{forkPIO4}
def idris_Python_46_Lib_46_Threading_46__123_forkPIO4_125_(in2, in6):
  while True:
    return (65771, None, None, in2)  # {U_io_return1}

# Main.{main4}
def idris_Main_46__123_main4_125_(in15, in16):
  while True:
    return (65676, in15, in16)  # {U_Main.{main3}1}

# Python.Prim.{next4}
def idris_Python_46_Prim_46__123_next4_125_(in4):
  while True:
    return (65756,)  # {U_Python.Prim.{next3}1}

# {Python.Prim.iterate, iter_lam5}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam5_125_(in3):
  while True:
    return (65784,)  # {U_{Python.Prim.iterate, iter_lam4}1}

# Python.Exceptions.{catch5}
def idris_Python_46_Exceptions_46__123_catch5_125_(in3):
  while True:
    return (65725,)  # {U_Python.Exceptions.{catch4}1}

# Python.Lib.Threading.{forkPIO5}
def idris_Python_46_Lib_46_Threading_46__123_forkPIO5_125_(in2, in5):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__36__58_(
        None,
        None,
        (0,),  # Python.Telescope.Empty
        idris_Python_46__47__46_(None, None, in5, "start", None),
        Unit
      ),
      (65739, in2)  # {U_Python.Lib.Threading.{forkPIO4}1}
    )

# Main.{main5}
def idris_Main_46__123_main5_125_(in15):
  while True:
    return (65687, in15)  # {U_Main.{main4}1}

# Python.Prim.{next5}
def idris_Python_46_Prim_46__123_next5_125_(in3):
  while True:
    return (65757,)  # {U_Python.Prim.{next4}1}

# {Python.Prim.iterate, iter_lam6}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam6_125_(e7, e9, in8):
  while True:
    return idris_Python_46_Prim_46_iterate_58_iter_58_0(
      None, None, None, None, None, None, None, e7, in8, e9
    )

# Python.Exceptions.{catch6}
def idris_Python_46_Exceptions_46__123_catch6_125_(e2, in0):
  while True:
    if in0[0] == 1:  # Python.Exceptions.Except
      in7, in8, = in0[1:]
      aux1 = APPLY0(APPLY0(e2, in7), in8)
    elif in0[0] == 0:  # Python.Exceptions.OK
      in9, = in0[1:]
      aux2 = (0, (65722,), (65726,))  # constructor of Prelude.Monad.Monad, {U_Python.Exceptions.{catch1}1}, {U_Python.Exceptions.{catch5}1}
      if aux2[0] == 0:  # constructor of Prelude.Monad.Monad
        in10, in11, = aux2[1:]
        aux3 = in10
      aux1 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux3), in9)
    return aux1

# Python.Lib.Threading.{forkPIO6}
def idris_Python_46_Lib_46_Threading_46__123_forkPIO6_125_(e1, in2):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__36__58_(
        None,
        None,
        (1, (0,), (65738,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO3}1}
        idris_Python_46__47__58_(
          None,
          None,
          idris_Python_46_Lib_46_Threading_46_import_95_(),
          "Thread",
          None
        ),
        (
          0,  # Builtins.MkSigma
          None,
          (
            0,  # Builtins.MkSigma
            idris_Python_46_marshalPIO(
              None,
              idris_Python_46_Lib_46_Threading_46_forkPIO_58_worker_58_0(None, e1, in2)
            ),
            Unit
          )
        )
      ),
      (65740, in2)  # {U_Python.Lib.Threading.{forkPIO5}1}
    )

# Main.{main6}
def idris_Main_46__123_main6_125_(in14):
  while True:
    return (65698,)  # {U_Main.{main5}1}

# Python.Prim.{next6}
def idris_Python_46_Prim_46__123_next6_125_(in2):
  while True:
    return (65771, None, None, in2)  # {U_io_return1}

# {Python.Prim.iterate, iter_lam7}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam7_125_(in2):
  while True:
    return (65771, None, None, in2)  # {U_io_return1}

# Main.{main7}
def idris_Main_46__123_main7_125_(in13):
  while True:
    return (65709,)  # {U_Main.{main6}1}

# Python.Prim.{next7}
def idris_Python_46_Prim_46__123_next7_125_(in1):
  while True:
    return (65759,)  # {U_Python.Prim.{next6}1}

# {Python.Prim.iterate, iter_lam8}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam8_125_(in1):
  while True:
    return (65787,)  # {U_{Python.Prim.iterate, iter_lam7}1}

# Main.{main8}
def idris_Main_46__123_main8_125_(in18, in19):
  while True:
    return in18 + in19

# Python.Prim.{next8}
def idris_Python_46_Prim_46__123_next8_125_(in5, in6):
  while True:
    return (65770, None, None, None, in5, in6)  # {U_io_bind1}

# {Python.Prim.iterate, iter_lam9}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam9_125_(in5, in6):
  while True:
    return (65770, None, None, None, in5, in6)  # {U_io_bind1}

# Main.{main9}
def idris_Main_46__123_main9_125_(in18):
  while True:
    return (65711, in18)  # {U_Main.{main8}1}

# Python.Prim.{next9}
def idris_Python_46_Prim_46__123_next9_125_(in5):
  while True:
    return (65761, in5)  # {U_Python.Prim.{next8}1}

# {Python.Prim.iterate, iter_lam10}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam10_125_(in5):
  while True:
    return (65789, in5)  # {U_{Python.Prim.iterate, iter_lam9}1}

# Main.{main10}
def idris_Main_46__123_main10_125_(in12):
  while True:
    return idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
      None,
      None,
      None,
      idris_Prelude_46_Foldable_46_concat(None, None, (65710,), (0, (65712,), "")),  # {U_Main.{main7}1}, constructor of Prelude.Algebra.Monoid, {U_Main.{main9}1}
      in12
    )

# Python.Prim.{next10}
def idris_Python_46_Prim_46__123_next10_125_(in4):
  while True:
    return (65762,)  # {U_Python.Prim.{next9}1}

# {Python.Prim.iterate, iter_lam11}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam11_125_(in4):
  while True:
    return (65777,)  # {U_{Python.Prim.iterate, iter_lam10}1}

# Main.{main11}
def idris_Main_46__123_main11_125_(in10, in21):
  while True:
    return (65771, None, None, in10 + 1)  # {U_io_return1}

# Python.Prim.{next11}
def idris_Python_46_Prim_46__123_next11_125_(in3):
  while True:
    return (65751,)  # {U_Python.Prim.{next10}1}

# {Python.Prim.iterate, iter_lam12}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam12_125_(in3):
  while True:
    return (65778,)  # {U_{Python.Prim.iterate, iter_lam11}1}

# Main.{main12}
def idris_Main_46__123_main12_125_(in10, in20):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Prelude_46_putStr(None, str(in10 + 1) + ". " + in20 + "\n"),
      (65645, in10)  # {U_Main.{main11}1}
    )

# Python.Prim.{next12}
def idris_Python_46_Prim_46__123_next12_125_(in0):
  while True:
    if in0[0] == 1:  # Python.Exceptions.Except
      in7, in8, = in0[1:]
      if in7[0] == 0:  # Python.Exceptions.StopIteration
        aux3 = (0, (65754,), (65758,))  # constructor of Prelude.Monad.Monad, {U_Python.Prim.{next1}1}, {U_Python.Prim.{next5}1}
        if aux3[0] == 0:  # constructor of Prelude.Monad.Monad
          in9, in10, = aux3[1:]
          aux4 = in9
        aux2 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux4), None)
      else:
        aux2 = idris_Python_46_Exceptions_46_raise(None, in8)
      aux1 = aux2
    elif in0[0] == 0:  # Python.Exceptions.OK
      in11, = in0[1:]
      aux5 = (0, (65760,), (65752,))  # constructor of Prelude.Monad.Monad, {U_Python.Prim.{next7}1}, {U_Python.Prim.{next11}1}
      if aux5[0] == 0:  # constructor of Prelude.Monad.Monad
        in12, in13, = aux5[1:]
        aux6 = in12
      aux1 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux6), in11)
    return aux1

# {Python.Prim.iterate, iter_lam13}
def idris__123_Python_46_Prim_46_iterate_44__32_iter_95_lam13_125_(e9, e8, e7, in0):
  while True:
    if in0 is not None:  # Prelude.Maybe.Just
      in7 = in0
      aux1 = APPLY0(
        APPLY0(
          idris_Prelude_46_Monad_46__62__62__61_(
            None,
            None,
            None,
            (0, (65781,), (65785,))  # constructor of Prelude.Monad.Monad, {U_{Python.Prim.iterate, iter_lam1}1}, {U_{Python.Prim.iterate, iter_lam5}1}
          ),
          APPLY0(APPLY0(e9, e8), in7)
        ),
        (65786, e7, e9)  # {U_{Python.Prim.iterate, iter_lam6}1}
      )
    elif in0 is None:  # Prelude.Maybe.Nothing
      aux2 = (0, (65788,), (65779,))  # constructor of Prelude.Monad.Monad, {U_{Python.Prim.iterate, iter_lam8}1}, {U_{Python.Prim.iterate, iter_lam12}1}
      if aux2[0] == 0:  # constructor of Prelude.Monad.Monad
        in9, in10, = aux2[1:]
        aux3 = in9
      aux1 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux3), e8)
    return aux1

# Main.{main13}
def idris_Main_46__123_main13_125_(in10, in11):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      (
        65770,  # {U_io_bind1}
        None,
        None,
        None,
        idris_Python_46__62__58_(
          None,
          idris_Python_46__47__46_(None, None, in11, "strings", None),
          None,
          None
        ),
        (65713, None, None, None, (65644,), (65743, None))  # {U_Prelude.Basics..1}, {U_Main.{main10}1}, {U_Python.Prim.collect1}
      ),
      (65646, in10)  # {U_Main.{main12}1}
    )

# Main.{main14}
def idris_Main_46__123_main14_125_(in10):
  while True:
    return (65647, in10)  # {U_Main.{main13}1}

# Main.{main15}
def idris_Main_46__123_main15_125_(in28):
  while True:
    return (65771, None, None, in28)  # {U_io_return1}

# Main.{main16}
def idris_Main_46__123_main16_125_(in27):
  while True:
    return (65649,)  # {U_Main.{main15}1}

# Main.{main17}
def idris_Main_46__123_main17_125_(in31, in32):
  while True:
    return (65770, None, None, None, in31, in32)  # {U_io_bind1}

# Main.{main18}
def idris_Main_46__123_main18_125_(in31):
  while True:
    return (65651, in31)  # {U_Main.{main17}1}

# Main.{main19}
def idris_Main_46__123_main19_125_(in30):
  while True:
    return (65652,)  # {U_Main.{main18}1}

# Main.{main20}
def idris_Main_46__123_main20_125_(in29):
  while True:
    return (65653,)  # {U_Main.{main19}1}

# Main.{main21}
def idris_Main_46__123_main21_125_(in28):
  while True:
    return (65771, None, None, in28)  # {U_io_return1}

# Main.{main22}
def idris_Main_46__123_main22_125_(in27):
  while True:
    return (65656,)  # {U_Main.{main21}1}

# Main.{main23}
def idris_Main_46__123_main23_125_(in31, in32):
  while True:
    return (65770, None, None, None, in31, in32)  # {U_io_bind1}

# Main.{main24}
def idris_Main_46__123_main24_125_(in31):
  while True:
    return (65658, in31)  # {U_Main.{main23}1}

# Main.{main25}
def idris_Main_46__123_main25_125_(in30):
  while True:
    return (65659,)  # {U_Main.{main24}1}

# Main.{main26}
def idris_Main_46__123_main26_125_(in29):
  while True:
    return (65660,)  # {U_Main.{main25}1}

# Main.{main27}
def idris_Main_46__123_main27_125_(in34):
  while True:
    return (0,)  # Python.Telescope.Empty

# Main.{main28}
def idris_Main_46__123_main28_125_(in28):
  while True:
    return (65771, None, None, in28)  # {U_io_return1}

# Main.{main29}
def idris_Main_46__123_main29_125_(in27):
  while True:
    return (65663,)  # {U_Main.{main28}1}

# Main.{main30}
def idris_Main_46__123_main30_125_(in31, in32):
  while True:
    return (65770, None, None, None, in31, in32)  # {U_io_bind1}

# Main.{main31}
def idris_Main_46__123_main31_125_(in31):
  while True:
    return (65666, in31)  # {U_Main.{main30}1}

# Main.{main32}
def idris_Main_46__123_main32_125_(in30):
  while True:
    return (65667,)  # {U_Main.{main31}1}

# Main.{main33}
def idris_Main_46__123_main33_125_(in29):
  while True:
    return (65668,)  # {U_Main.{main32}1}

# Main.{main34}
def idris_Main_46__123_main34_125_(in28):
  while True:
    return (65771, None, None, in28)  # {U_io_return1}

# Main.{main35}
def idris_Main_46__123_main35_125_(in27):
  while True:
    return (65670,)  # {U_Main.{main34}1}

# Main.{main36}
def idris_Main_46__123_main36_125_(in31, in32):
  while True:
    return (65770, None, None, None, in31, in32)  # {U_io_bind1}

# Main.{main37}
def idris_Main_46__123_main37_125_(in31):
  while True:
    return (65672, in31)  # {U_Main.{main36}1}

# Main.{main38}
def idris_Main_46__123_main38_125_(in30):
  while True:
    return (65673,)  # {U_Main.{main37}1}

# Main.{main39}
def idris_Main_46__123_main39_125_(in29):
  while True:
    return (65674,)  # {U_Main.{main38}1}

# Main.{main40}
def idris_Main_46__123_main40_125_(in35, in36):
  while True:
    aux1 = (0, (65671,), (65675,))  # constructor of Prelude.Monad.Monad, {U_Main.{main35}1}, {U_Main.{main39}1}
    if aux1[0] == 0:  # constructor of Prelude.Monad.Monad
      in37, in38, = aux1[1:]
      aux2 = in37
    return APPLY0(
      idris_Prelude_46_Applicative_46_pure(None, None, aux2),
      APPLY0(idris_Prelude_46_Strings_46_length(), in35)
    )

# Main.{main41}
def idris_Main_46__123_main41_125_(in26, in35):
  while True:
    return APPLY0(
      APPLY0(
        idris_Prelude_46_Monad_46__62__62__61_(
          None,
          None,
          None,
          (0, (65664,), (65669,))  # constructor of Prelude.Monad.Monad, {U_Main.{main29}1}, {U_Main.{main33}1}
        ),
        idris_Prelude_46_putStr(None, "thread " + in26 + " done" + "\n")
      ),
      (65677, in35)  # {U_Main.{main40}1}
    )

# Main.{main42}
def idris_Main_46__123_main42_125_(in1, in26, in33):
  while True:
    return APPLY0(
      APPLY0(
        idris_Prelude_46_Monad_46__62__62__61_(
          None,
          None,
          None,
          (0, (65657,), (65661,))  # constructor of Prelude.Monad.Monad, {U_Main.{main22}1}, {U_Main.{main26}1}
        ),
        idris_Python_46__47__58_(
          None,
          None,
          idris_Python_46__36__58_(
            None,
            None,
            (1, (0,), (65662,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Main.{main27}1}
            idris_Python_46__47__46_(None, None, in1, "get", None),
            (0, "http://idris-lang.org", Unit)  # Builtins.MkSigma
          ),
          "text",
          None
        )
      ),
      (65678, in26)  # {U_Main.{main41}1}
    )

# Main.{main43}
def idris_Main_46__123_main43_125_(in1, in26):
  while True:
    return APPLY0(
      APPLY0(
        idris_Prelude_46_Monad_46__62__62__61_(
          None,
          None,
          None,
          (0, (65650,), (65655,))  # constructor of Prelude.Monad.Monad, {U_Main.{main16}1}, {U_Main.{main20}1}
        ),
        idris_Prelude_46_putStr(None, "thread " + in26 + " starting" + "\n")
      ),
      (65679, in1, in26)  # {U_Main.{main42}1}
    )

# Main.{main44}
def idris_Main_46__123_main44_125_(in48):
  while True:
    return (0,)  # Python.Telescope.Empty

# Main.{main45}
def idris_Main_46__123_main45_125_(in49):
  while True:
    return idris_Prelude_46_putStr(
      None,
      "Something's wrong, your root's homedir is writable!\n"
    )

# Main.{main46}
def idris_Main_46__123_main46_125_(in50, in51):
  while True:
    if in50[0] == 11:  # Python.Exceptions.OSError
      aux1 = idris_Prelude_46_putStr(
        None,
        "  -> (1) everything's fine: " + idris_Python_46_Exceptions_46_showException(in51) + "\n"
      )
    else:
      aux1 = idris_Python_46_Exceptions_46_raise(None, in51)
    return aux1

# Main.{main47}
def idris_Main_46__123_main47_125_(in50):
  while True:
    return (65683, in50)  # {U_Main.{main46}1}

# Main.{main48}
def idris_Main_46__123_main48_125_(in53):
  while True:
    return (0,)  # Python.Telescope.Empty

# Main.{main49}
def idris_Main_46__123_main49_125_(in54):
  while True:
    if in54[0] == 1:  # Python.Exceptions.Except
      in55, in56, = in54[1:]
      if in55[0] == 11:  # Python.Exceptions.OSError
        aux2 = idris_Prelude_46_putStr(
          None,
          "  -> (2) everything's fine: " + idris_Python_46_Exceptions_46_showException(in56) + "\n"
        )
      else:
        aux2 = idris_Python_46_Exceptions_46_raise(None, in56)
      aux1 = aux2
    elif in54[0] == 0:  # Python.Exceptions.OK
      in57, = in54[1:]
      aux1 = idris_Prelude_46_putStr(
        None,
        "Your root could probably use some security lessons!\n"
      )
    return aux1

# Main.{main50}
def idris_Main_46__123_main50_125_(in46, in52):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Exceptions_46_try(
        None,
        idris_Python_46__36__58_(
          None,
          None,
          (1, (0,), (65685,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Main.{main48}1}
          idris_Python_46__47__46_(None, None, in46, "mkdir", None),
          (0, "/root/hello", Unit)  # Builtins.MkSigma
        )
      ),
      (65686,)  # {U_Main.{main49}1}
    )

# Main.{main51}
def idris_Main_46__123_main51_125_(in46, in47):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Exceptions_46_catch(
        None,
        idris_Python_46_Exceptions_46_try(
          None,
          (
            65770,  # {U_io_bind1}
            None,
            None,
            None,
            idris_Python_46__36__58_(
              None,
              None,
              (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Main.{main44}1}
              idris_Python_46__47__46_(None, None, in46, "mkdir", None),
              (0, "/root/hello", Unit)  # Builtins.MkSigma
            ),
            (65682,)  # {U_Main.{main45}1}
          )
        ),
        (65684,)  # {U_Main.{main47}1}
      ),
      (65688, in46)  # {U_Main.{main50}1}
    )

# Main.{main52}
def idris_Main_46__123_main52_125_(in46):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Prelude_46_putStr(None, "And now, let's fail!\n"),
      (65689, in46)  # {U_Main.{main51}1}
    )

# Main.{main53}
def idris_Main_46__123_main53_125_(in45):
  while True:
    return (65770, None, None, None, idris_Python_46_Lib_46_Os_46_import_95_(), (65690,))  # {U_io_bind1}, {U_Main.{main52}1}

# Main.{main54}
def idris_Main_46__123_main54_125_(in44):
  while True:
    return (65770, None, None, None, idris_Prelude_46_putStr(None, "\n"), (65691,))  # {U_io_bind1}, {U_Main.{main53}1}

# Main.{main55}
def idris_Main_46__123_main55_125_(in42, in43):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Prelude_46_putStr(
        None,
        "thread B says " + idris_Prelude_46_Prelude_46__64_Prelude_46_Show_36_Nat_58__33_show_58_0(in42) + "\n"
      ),
      (65692,)  # {U_Main.{main54}1}
    )

# Main.{main56}
def idris_Main_46__123_main56_125_(in41, in42):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Prelude_46_putStr(
        None,
        "thread A says " + idris_Prelude_46_Prelude_46__64_Prelude_46_Show_36_Nat_58__33_show_58_0(in41) + "\n"
      ),
      (65693, in42)  # {U_Main.{main55}1}
    )

# Main.{main57}
def idris_Main_46__123_main57_125_(in40, in41):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Lib_46_Threading_46_wait(None, in40),
      (65694, in41)  # {U_Main.{main56}1}
    )

# Main.{main58}
def idris_Main_46__123_main58_125_(in39, in40):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Lib_46_Threading_46_wait(None, in39),
      (65695, in40)  # {U_Main.{main57}1}
    )

# Main.{main59}
def idris_Main_46__123_main59_125_(in25, in39):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Lib_46_Threading_46_forkPIO(None, APPLY0(in25, "B")),
      (65696, in39)  # {U_Main.{main58}1}
    )

# Main.{main60}
def idris_Main_46__123_main60_125_(in1, in24):
  while True:
    in25 = (65680, in1)  # {U_Main.{main43}1}
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Lib_46_Threading_46_forkPIO(None, APPLY0(in25, "A")),
      (65697, in25)  # {U_Main.{main59}1}
    )

# Main.{main61}
def idris_Main_46__123_main61_125_(in1, in23):
  while True:
    return (65770, None, None, None, idris_Prelude_46_putStr(None, "\n"), (65699, in1))  # {U_io_bind1}, {U_Main.{main60}1}

# Main.{main62}
def idris_Main_46__123_main62_125_(in1, in22):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Prelude_46_putStr(None, "Total number of features: " + str(in22) + "\n"),
      (65700, in1)  # {U_Main.{main61}1}
    )

# Main.{main63}
def idris_Main_46__123_main63_125_(in8, in1, in9):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Prim_46_iterate(None, None, in8, 0, (65648,)),  # {U_Main.{main14}1}
      (65701, in1)  # {U_Main.{main62}1}
    )

# Main.{main64}
def idris_Main_46__123_main64_125_(in1, in8):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Prelude_46_putStr(
        None,
        "Idris has got the following exciting features:\n"
      ),
      (65702, in8, in1)  # {U_Main.{main63}1}
    )

# Main.{main65}
def idris_Main_46__123_main65_125_(in1, in6):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__62__58_(
        None,
        idris_Python_46__36__58_(
          None,
          None,
          (1, (0,), (65665,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Main.{main2}1}
          idris_Python_46__47__46_(None, None, in6, "select", None),
          (0, "div.entry-content li", Unit)  # Builtins.MkSigma
        ),
        None,
        None
      ),
      (65703, in1)  # {U_Main.{main64}1}
    )

# Main.{main66}
def idris_Main_46__123_main66_125_(in3, in1, in4):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__36__58_(
        None,
        None,
        (1, (0,), (65654,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Main.{main1}1}
        idris_Python_46__47__46_(None, None, in4, "BeautifulSoup", None),
        (0, in3, Unit)  # Builtins.MkSigma
      ),
      (65704, in1)  # {U_Main.{main65}1}
    )

# Main.{main67}
def idris_Main_46__123_main67_125_(in1, in3):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Lib_46_BeautifulSoup_46_import_95_(),
      (65705, in3, in1)  # {U_Main.{main66}1}
    )

# Main.{main68}
def idris_Main_46__123_main68_125_(in1):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__47__58_(
        None,
        None,
        idris_Python_46__36__58_(
          None,
          None,
          (1, (0,), (65643,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Main.{main0}1}
          idris_Python_46__47__46_(None, None, in1, "get", None),
          (0, "http://idris-lang.org", Unit)  # Builtins.MkSigma
        ),
        "text",
        None
      ),
      (65706, in1)  # {U_Main.{main67}1}
    )

# Main.{main69}
def idris_Main_46__123_main69_125_(in0):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46__36__58_(
        None,
        None,
        (0,),  # Python.Telescope.Empty
        idris_Python_46__47__46_(None, None, in0, "Session", None),
        Unit
      ),
      (65707,)  # {U_Main.{main68}1}
    )

# Python.Lib.Threading.forkPIO, worker
def idris_Python_46_Lib_46_Threading_46_forkPIO_58_worker_58_0(e0, e1, e2):
  while True:
    return (65770, None, None, None, e1, (65775, e2))  # {U_io_bind1}, {U_{Python.Lib.Threading.forkPIO, worker_lam1}1}

# Python.Prim.iterate, iter
def idris_Python_46_Prim_46_iterate_58_iter_58_0(
  e0, e1, e2, e3, e4, e5, e6, e7, e8, e9
):
  while True:
    return (
      65770,  # {U_io_bind1}
      None,
      None,
      None,
      idris_Python_46_Prim_46_next(None, e7),
      (65780, e9, e8, e7)  # {U_{Python.Prim.iterate, iter_lam13}1}
    )

# Prelude.List.reverse, reverse'
def idris_Prelude_46_List_46_reverse_58_reverse_39__58_0(e0, e1, e2):
  while True:
    if e2:  # Prelude.List.::
      in0, in1 = e2.head, e2.tail
      e0, e1, e2, = None, e1.cons(in0), in1,
      continue
      aux1 = idris_error("unreachable due to tail call")
    elif not e2:  # Prelude.List.Nil
      aux1 = e1
    return aux1

# Decidable.Equality.Decidable.Equality.Char instance of Decidable.Equality.DecEq, method decEq, primitiveNotEq
def idris_Decidable_46_Equality_46_Decidable_46_Equality_46__64_Decidable_46_Equality_46_DecEq_36_Char_58__33_decEq_58_0_58_primitiveNotEq_58_0():
  while True:
    return None

# Decidable.Equality.Decidable.Equality.Int instance of Decidable.Equality.DecEq, method decEq, primitiveNotEq
def idris_Decidable_46_Equality_46_Decidable_46_Equality_46__64_Decidable_46_Equality_46_DecEq_36_Int_58__33_decEq_58_0_58_primitiveNotEq_58_0():
  while True:
    return None

# Decidable.Equality.Decidable.Equality.Integer instance of Decidable.Equality.DecEq, method decEq, primitiveNotEq
def idris_Decidable_46_Equality_46_Decidable_46_Equality_46__64_Decidable_46_Equality_46_DecEq_36_Integer_58__33_decEq_58_0_58_primitiveNotEq_58_0():
  while True:
    return None

# Decidable.Equality.Decidable.Equality.String instance of Decidable.Equality.DecEq, method decEq, primitiveNotEq
def idris_Decidable_46_Equality_46_Decidable_46_Equality_46__64_Decidable_46_Equality_46_DecEq_36_String_58__33_decEq_58_0_58_primitiveNotEq_58_0():
  while True:
    return None

# Prelude.Foldable.Prelude.List.List instance of Prelude.Foldable.Foldable, method foldr
def idris_Prelude_46_Foldable_46_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List_58__33_foldr_58_0(
  e0, e1, e2, e3, e4
):
  while True:
    if e4:  # Prelude.List.::
      in0, in1 = e4.head, e4.tail
      aux1 = APPLY0(
        APPLY0(e2, in0),
        APPLY0(
          APPLY0(
            APPLY0(idris_Prelude_46_Foldable_46_foldr(None, None, None, (65795,)), e2),  # {U_Prelude.List.List instance of Prelude.Foldable.Foldable5}
            e3
          ),
          in1
        )
      )
    elif not e4:  # Prelude.List.Nil
      aux1 = e3
    return aux1

# Prelude.Functor.Prelude.IO' ffi instance of Prelude.Functor.Functor, method map
def idris_Prelude_46_Functor_46_Prelude_46__64_Prelude_46_Functor_46_Functor_36_IO_39__32_ffi_58__33_map_58_0(
  e0, e1, e2, e3, e4
):
  while True:
    return (65770, None, None, None, e4, (65714, e3))  # {U_io_bind1}, {U_Prelude.Functor.{Prelude.IO' ffi instance of Prelude.Functor.Functor, method map_lam0}1}

# Prelude.Prelude.Nat instance of Prelude.Show, method show
def idris_Prelude_46_Prelude_46__64_Prelude_46_Show_36_Nat_58__33_show_58_0(e0):
  while True:
    return str(e0)

# with block in Python.Telescope.strip
def idris__95_Python_46_Telescope_46_strip_95_with_95_16(e0, e1, e2, e3, e4, e5, e6):
  while True:
    if e1 is not None:  # Prelude.Maybe.Just
      in0 = e1
      aux1 = idris_Python_46_Telescope_46_strip(None, APPLY0(e6, in0), e4).cons(in0)
    elif e1 is None:  # Prelude.Maybe.Nothing
      aux1 = idris_Python_46_Telescope_46_strip(None, APPLY0(e6, None), e4).cons(None)
    return aux1

# Prelude.List.List instance of Prelude.Foldable.Foldable
def idris_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List(
  meth0, meth1, meth2, meth3, meth4
):
  while True:
    return idris_Prelude_46_Foldable_46_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List_58__33_foldr_58_0(
      None, None, meth2, meth3, meth4
    )

# case block in Void
def idris_Void_95_case():
  while True:
    return None

# Python.Exceptions.case block in catch
def idris_Python_46_Exceptions_46_catch_95_case(e0, e1, e2, e3, e4, e5):
  while True:
    if e4[0] == 1:  # Python.Exceptions.Except
      in0, in1, = e4[1:]
      aux1 = APPLY0(APPLY0(e2, in0), in1)
    elif e4[0] == 0:  # Python.Exceptions.OK
      in2, = e4[1:]
      if e3[0] == 0:  # constructor of Prelude.Monad.Monad
        in3, in4, = e3[1:]
        aux2 = in3
      aux1 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux2), in2)
    return aux1

# Python.Exceptions.case block in fromString
def idris_Python_46_Exceptions_46_fromString_95_case(e0, e1):
  while True:
    return {
      "ArithmeticError": (3,),  # Python.Exceptions.ArithmeticError
      "AssertionError": (7,),  # Python.Exceptions.AssertionError
      "AttributeError": (8,),  # Python.Exceptions.AttributeError
      "BufferError": (2,),  # Python.Exceptions.BufferError
      "EOFError": (14,),  # Python.Exceptions.EOFError
      "EnvironmentError": (9,),  # Python.Exceptions.EnvironmentError
      "FloatingPointError": (4,),  # Python.Exceptions.FloatingPointError
      "IOError": (10,),  # Python.Exceptions.IOError
      "ImportError": (15,),  # Python.Exceptions.ImportError
      "IndentationError": (26,),  # Python.Exceptions.IndentationError
      "IndexError": (17,),  # Python.Exceptions.IndexError
      "KeyError": (18,),  # Python.Exceptions.KeyError
      "LookupError": (16,),  # Python.Exceptions.LookupError
      "MemoryError": (19,),  # Python.Exceptions.MemoryError
      "NameError": (20,),  # Python.Exceptions.NameError
      "NotImplementedError": (24,),  # Python.Exceptions.NotImplementedError
      "OSError": (11,),  # Python.Exceptions.OSError
      "OverflowError": (5,),  # Python.Exceptions.OverflowError
      "ReferenceError": (22,),  # Python.Exceptions.ReferenceError
      "RuntimeError": (23,),  # Python.Exceptions.RuntimeError
      "StandardError": (1,),  # Python.Exceptions.StandardError
      "StopIteration": (0,),  # Python.Exceptions.StopIteration
      "SyntaxError": (25,),  # Python.Exceptions.SyntaxError
      "SystemError": (28,),  # Python.Exceptions.SystemError
      "TabError": (27,),  # Python.Exceptions.TabError
      "TypeError": (29,),  # Python.Exceptions.TypeError
      "UnboundLocalError": (21,),  # Python.Exceptions.UnboundLocalError
      "UnicodeDecodeError": (32,),  # Python.Exceptions.UnicodeDecodeError
      "UnicodeEncodeError": (33,),  # Python.Exceptions.UnicodeEncodeError
      "UnicodeError": (31,),  # Python.Exceptions.UnicodeError
      "UnicodeTranslateError": (34,),  # Python.Exceptions.UnicodeTranslateError
      "VMSError": (13,),  # Python.Exceptions.VMSError
      "ValueError": (30,),  # Python.Exceptions.ValueError
      "WindowsError": (12,),  # Python.Exceptions.WindowsError
      "ZeroDivisionError": (6,)  # Python.Exceptions.ZeroDivisionError
    }.get(e0, (35,))  # Python.Exceptions.Other

# case block in io_bind
def idris_io_95_bind_95_case(e0, e1, e2, e3, e4, e5, e6, e7):
  while True:
    return APPLY0(e7, e5)

# Main.case block in main
def idris_Main_46_main_95_case(
  e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14,
  e15, e16, e17, e18, e19, e20, e21
):
  while True:
    return APPLY0(
      APPLY0(
        idris_Prelude_46_Monad_46__62__62__61_(None, None, None, e18),
        idris_Prelude_46_putStr(None, "thread " + e20 + " starting" + "\n")
      ),
      (65642, e18, e3, e20)  # {U_Main.{case block in main_lam3}1}
    )

# Main.case block in main1
def idris_Main_46_main1_95_case(
  e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14,
  e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27,
  e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40,
  e41, e42
):
  while True:
    if e40[0] == 11:  # Python.Exceptions.OSError
      aux1 = idris_Prelude_46_putStr(
        None,
        "  -> (1) everything's fine: " + idris_Python_46_Exceptions_46_showException(e41) + "\n"
      )
    else:
      aux1 = idris_Python_46_Exceptions_46_raise(None, e41)
    return aux1

# Main.case block in main2
def idris_Main_46_main2_95_case(
  e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14,
  e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27,
  e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40,
  e41, e42, e43
):
  while True:
    if e42[0] == 1:  # Python.Exceptions.Except
      in0, in1, = e42[1:]
      if in0[0] == 11:  # Python.Exceptions.OSError
        aux2 = idris_Prelude_46_putStr(
          None,
          "  -> (2) everything's fine: " + idris_Python_46_Exceptions_46_showException(in1) + "\n"
        )
      else:
        aux2 = idris_Python_46_Exceptions_46_raise(None, in1)
      aux1 = aux2
    elif e42[0] == 0:  # Python.Exceptions.OK
      in2, = e42[1:]
      aux1 = idris_Prelude_46_putStr(
        None,
        "Your root could probably use some security lessons!\n"
      )
    return aux1

# Python.Prim.case block in next
def idris_Python_46_Prim_46_next_95_case(e0, e1, e2, e3, e4):
  while True:
    if e3[0] == 1:  # Python.Exceptions.Except
      in0, in1, = e3[1:]
      if in0[0] == 0:  # Python.Exceptions.StopIteration
        if e2[0] == 0:  # constructor of Prelude.Monad.Monad
          in2, in3, = e2[1:]
          aux3 = in2
        aux2 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux3), None)
      else:
        aux2 = idris_Python_46_Exceptions_46_raise(None, in1)
      aux1 = aux2
    elif e3[0] == 0:  # Python.Exceptions.OK
      in4, = e3[1:]
      if e2[0] == 0:  # constructor of Prelude.Monad.Monad
        in5, in6, = e2[1:]
        aux4 = in5
      aux1 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux4), in4)
    return aux1

# Python.Exceptions.case block in try
def idris_Python_46_Exceptions_46_try_95_case(e0, e1, e2, e3, e4, e5, e6, lamp7):
  while True:
    return (
      1,  # Python.Exceptions.Except
      {
        "ArithmeticError": (3,),  # Python.Exceptions.ArithmeticError
        "AssertionError": (7,),  # Python.Exceptions.AssertionError
        "AttributeError": (8,),  # Python.Exceptions.AttributeError
        "BufferError": (2,),  # Python.Exceptions.BufferError
        "EOFError": (14,),  # Python.Exceptions.EOFError
        "EnvironmentError": (9,),  # Python.Exceptions.EnvironmentError
        "FloatingPointError": (4,),  # Python.Exceptions.FloatingPointError
        "IOError": (10,),  # Python.Exceptions.IOError
        "ImportError": (15,),  # Python.Exceptions.ImportError
        "IndentationError": (26,),  # Python.Exceptions.IndentationError
        "IndexError": (17,),  # Python.Exceptions.IndexError
        "KeyError": (18,),  # Python.Exceptions.KeyError
        "LookupError": (16,),  # Python.Exceptions.LookupError
        "MemoryError": (19,),  # Python.Exceptions.MemoryError
        "NameError": (20,),  # Python.Exceptions.NameError
        "NotImplementedError": (24,),  # Python.Exceptions.NotImplementedError
        "OSError": (11,),  # Python.Exceptions.OSError
        "OverflowError": (5,),  # Python.Exceptions.OverflowError
        "ReferenceError": (22,),  # Python.Exceptions.ReferenceError
        "RuntimeError": (23,),  # Python.Exceptions.RuntimeError
        "StandardError": (1,),  # Python.Exceptions.StandardError
        "StopIteration": (0,),  # Python.Exceptions.StopIteration
        "SyntaxError": (25,),  # Python.Exceptions.SyntaxError
        "SystemError": (28,),  # Python.Exceptions.SystemError
        "TabError": (27,),  # Python.Exceptions.TabError
        "TypeError": (29,),  # Python.Exceptions.TypeError
        "UnboundLocalError": (21,),  # Python.Exceptions.UnboundLocalError
        "UnicodeDecodeError": (32,),  # Python.Exceptions.UnicodeDecodeError
        "UnicodeEncodeError": (33,),  # Python.Exceptions.UnicodeEncodeError
        "UnicodeError": (31,),  # Python.Exceptions.UnicodeError
        "UnicodeTranslateError": (34,),  # Python.Exceptions.UnicodeTranslateError
        "VMSError": (13,),  # Python.Exceptions.VMSError
        "ValueError": (30,),  # Python.Exceptions.ValueError
        "WindowsError": (12,),  # Python.Exceptions.WindowsError
        "ZeroDivisionError": (6,)  # Python.Exceptions.ZeroDivisionError
      }.get(e5, (35,)),  # Python.Exceptions.Other
      lamp7
    )

# Python.Prim.case block in Python.Prim.iterate, iter
def idris_Python_46_Prim_46_Python_46_Prim_46_iterate_58_iter_58_0_95_case(
  e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12
):
  while True:
    if e11 is not None:  # Prelude.Maybe.Just
      in0 = e11
      aux1 = APPLY0(
        APPLY0(
          idris_Prelude_46_Monad_46__62__62__61_(None, None, None, e10),
          APPLY0(APPLY0(e9, e8), in0)
        ),
        (65744, e6, e9)  # {U_Python.Prim.{case block in Python.Prim.iterate, iter_lam0}1}
      )
    elif e11 is None:  # Prelude.Maybe.Nothing
      if e10[0] == 0:  # constructor of Prelude.Monad.Monad
        in2, in3, = e10[1:]
        aux2 = in2
      aux1 = APPLY0(idris_Prelude_46_Applicative_46_pure(None, None, aux2), e8)
    return aux1

# Main.case block in case block in main1
def idris_Main_46_main1_95_case_95_case(
  e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14,
  e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27,
  e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40,
  e41, e42, e43
):
  while True:
    if e40[0] == 11:  # Python.Exceptions.OSError
      aux1 = idris_Prelude_46_putStr(
        None,
        "  -> (1) everything's fine: " + idris_Python_46_Exceptions_46_showException(e41) + "\n"
      )
    else:
      aux1 = idris_Python_46_Exceptions_46_raise(None, e41)
    return aux1

# <<Void eliminator>>
def idris_Void_95_elim():
  while True:
    return None

if __name__ == '__main__':
  runMain0()
