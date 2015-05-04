module Python.Lib.Queue

import Python
import Data.Erased

%default total
%access public

Queue : Type -> Signature
Queue a = signature "Queue"
  [ "put" ::: [a] ~> ()
  , "get" ::: [Int] ~> a
  , "task_done" ::: [] ~> ()
  ]

QueueM : Signature
QueueM = signature "QueueM"
  [ "Queue" :::
      Function 
        (Bind (Forall Type) $ \a =>           -- Type of elements
          Bind (Default Int 0) $ \maxLen =>   -- Maximum size of queue
            Return $ Obj (Queue $ unerase a)  -- Returns a Queue of `a`
        )
  ]

import_ : PIO $ Obj QueueM
import_ = importModule "Queue"  -- this is lowercase in python3
