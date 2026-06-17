
from unittest import TestCase
from strand import (
    BaseStrand,
    PositiveStrand,
    NegativeStrand,
    UnknownStrand,
    Strand
)
from math import inf, nan


class TestCase000_PositiveStrand(TestCase):
    constructor = PositiveStrand
    intvalue_eq = 1
    strvalue_eq = '+'
    intvalue_ne = -1
    strvalue_ne = '-'

    def test__init__0(self):
        i = self.constructor()
        self.assertIsInstance(i, self.constructor)

    def test__bool__0(self):
        self.assertTrue(bool(self.constructor()))

    def test__int__0(self):
        self.assertEqual(int(self.constructor()), self.intvalue_eq)

    def test__str__0(self):
        self.assertEqual(str(self.constructor()), self.strvalue_eq)

    def test__eq__0(self):
        self.assertTrue(self.constructor() == self.intvalue_eq)
        self.assertTrue(self.constructor() == self.strvalue_eq)

    def test__eq__1(self):
        self.assertTrue(self.constructor() == self.constructor())

    def test__eq__2(self):
        self.assertFalse(self.constructor() == self.intvalue_ne)
        self.assertFalse(self.constructor() == self.strvalue_ne)
        
    def test__eq__3(self):
        with self.assertRaises(ValueError):
            self.constructor() == '='
            
    def test__eq__4(self):
        with self.assertRaises(TypeError):
            self.constructor() == ()
        with self.assertRaises(TypeError):
            self.constructor() == []

    def test__ne__0(self):
        self.assertTrue(self.constructor() != self.intvalue_ne)
        self.assertTrue(self.constructor() != self.strvalue_ne)

    def test__ne__1(self):
        self.assertFalse(self.constructor() != self.intvalue_eq)
        self.assertFalse(self.constructor() != self.strvalue_eq)
        
    def test__ne__2(self):
        with self.assertRaises(ValueError):
            self.constructor() != '?'
        
    def test__ne__3(self):
        with self.assertRaises(TypeError):
            self.constructor() != ()
        with self.assertRaises(TypeError):
            self.constructor() != []
        
    def test__lt__0(self):
        self.assertFalse(self.constructor() < self.constructor())

    def test__lt__1(self):
        self.assertFalse(self.constructor() < 0)
        self.assertFalse(self.constructor() < '.')

    def test__lt__2(self):
        with self.assertRaises(ValueError):
            self.constructor() < '='

    def test__le__0(self):
        self.assertTrue(self.constructor() <= self.constructor())

    def test__le__1(self):
        self.assertFalse(self.constructor() <= 0)
        self.assertFalse(self.constructor() <= '.')

    def test__le__2(self):
        with self.assertRaises(ValueError):
            self.constructor() <= '='

    def test__le__3(self):
        self.assertTrue(self.constructor() <= self.intvalue_eq)
        self.assertTrue(self.constructor() <= self.strvalue_eq)
            
    def test__gt__0(self):
        self.assertFalse(self.constructor() > self.constructor())

    def test__gt__1(self):
        self.assertTrue(self.constructor() > 0)
        self.assertTrue(self.constructor() > '.')
        
    def test__gt__2(self):
        with self.assertRaises(ValueError):
            self.constructor() > '='

    def test__ge__0(self):
        self.assertTrue(self.constructor() >= self.constructor())

    def test__ge__1(self):
        self.assertTrue(self.constructor() >= 0)
        self.assertTrue(self.constructor() >= '.')
        
    def test__ge__2(self):
        with self.assertRaises(ValueError):
            self.constructor() >= '='

    def test__ge__3(self):
         self.assertTrue(self.constructor() >= self.intvalue_eq)
         self.assertTrue(self.constructor() >= self.strvalue_eq)

    def test__mul__0(self):
        self.assertTrue(self.constructor() * self.constructor() > 0)

    def test__mul__1(self):
        self.assertTrue((self.constructor() * 1) == self.constructor())

    def test__mul__2(self):
        self.assertTrue((self.constructor() * self.intvalue_eq) > 0)
        self.assertTrue((self.constructor() * self.strvalue_eq) > 0)

    def test__mul__3(self):
        self.assertTrue((self.constructor() * self.intvalue_ne) < 0)
        self.assertTrue((self.constructor() * self.strvalue_ne) < 0)

    def test__mul__4(self):
        self.assertEqual(self.constructor() * 0, 0)
        self.assertEqual(self.constructor() * '.', '.')
        
    def test__index__0(self):
        l = ['.','+','-']
        self.assertEqual(l[self.constructor()], self.strvalue_eq)

    def test__pos__0(self):
        self.assertEqual(+self.constructor(), self.constructor())
        self.assertEqual(+self.constructor(), self.strvalue_eq)
        self.assertEqual(+self.constructor(), self.intvalue_eq)

    def test__neg__0(self):
        self.assertEqual(-self.constructor(), self.strvalue_ne)
        self.assertEqual(-self.constructor(), self.intvalue_ne)
        
    def test__reversed__0(self):
        self.assertNotEqual(reversed(self.constructor()), self.constructor())

    def test__reversed__1(self):
        self.assertEqual(reversed(self.constructor()), self.intvalue_ne)
        self.assertEqual(reversed(self.constructor()), self.strvalue_ne)

    def test_ispositive_0(self):
        self.assertEqual(self.constructor().ispositive(), self.intvalue_eq == 1)
        self.assertNotEqual(self.constructor().ispositive(), self.intvalue_ne == 1)

    def test_isnegative_0(self):
        self.assertEqual(self.constructor().isnegative(), self.intvalue_eq == -1)
        self.assertNotEqual(self.constructor().isnegative(), self.intvalue_ne == -1)

    def test_isunknown_0(self):
        self.assertFalse(self.constructor().isunknown())

        
class TestCase001_NegativeStrand(TestCase000_PositiveStrand):
    constructor = NegativeStrand
    intvalue_eq = -1
    strvalue_eq = '-'
    intvalue_ne = 1
    strvalue_ne = '+'
    
    def test__lt__1(self):
        self.assertTrue(self.constructor() < 0)
        self.assertTrue(self.constructor() < '.')

    def test__le__1(self):
        self.assertTrue(self.constructor() <= 0)
        self.assertTrue(self.constructor() <= '.')

    def test__gt__1(self):
        self.assertFalse(self.constructor() > 0)
        self.assertFalse(self.constructor() > '.')
        
    def test__ge__1(self):
        self.assertFalse(self.constructor() >= 0)
        self.assertFalse(self.constructor() >= '.')
        


class TestCase002_UnknownStrand(TestCase000_PositiveStrand):
    constructor = UnknownStrand
    intvalue_eq = 0
    strvalue_eq = '.'
    intvalue_ne = 0
    strvalue_ne = '.'
    
    def test__bool__0(self):
        self.assertFalse(bool(self.constructor()))

    def test__eq__2(self):
        self.assertTrue(self.constructor() == self.intvalue_ne)
        self.assertTrue(self.constructor() == self.strvalue_ne)        

    def test__ne__0(self):
        self.assertFalse(self.constructor() != self.intvalue_ne)
        self.assertFalse(self.constructor() != self.strvalue_ne)

    def test__ne__1(self):
        self.assertFalse(self.constructor() != self.intvalue_eq)
        self.assertFalse(self.constructor() != self.strvalue_eq)

    def test__le__1(self):
        self.assertTrue(self.constructor() <= 0)
        self.assertTrue(self.constructor() <= '.')

    def test__gt__1(self):
        self.assertFalse(self.constructor() > 0)
        self.assertFalse(self.constructor() > '.')

    def test__mul__0(self):
        self.assertTrue(self.constructor() * self.constructor() == 0)

    def test__mul__2(self):
        self.assertFalse((self.constructor() * self.intvalue_eq) > 0)
        self.assertFalse((self.constructor() * self.strvalue_eq) > 0)

    def test__mul__3(self):
        self.assertFalse((self.constructor() * self.intvalue_ne) < 0)
        self.assertFalse((self.constructor() * self.strvalue_ne) < 0)

    def test__mul__4(self):
        self.assertEqual(self.constructor() * 0, 0)
        self.assertEqual(self.constructor() * '.', '.')

    def test__reversed__0(self):
        self.assertEqual(reversed(self.constructor()), self.constructor())

    def test_ispositive_0(self):
        self.assertEqual(self.constructor().ispositive(), self.intvalue_eq == 1)
        self.assertEqual(self.constructor().ispositive(), self.intvalue_ne == 1)

    def test_isnegative_0(self):
        self.assertEqual(self.constructor().isnegative(), self.intvalue_eq == -1)
        self.assertEqual(self.constructor().isnegative(), self.intvalue_ne == -1)

    def test_isunknown_0(self):
        self.assertTrue(self.constructor().isunknown())
    
