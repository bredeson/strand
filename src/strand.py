
import math as _math


_STRAND = {}


class BaseStrand(object):
    __slots__ = ()
    def __bool__(self):
        return bool(self.int)
    
    def __int__(self):
        return self.int

    def __str__(self):
        return self.str

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.str)
    
    def __eq__(self, other):
        if not isinstance(other, BaseStrand):
            other = Strand(other)
        return self.int == other.int
    
    def __ne__(self, other):
        if not isinstance(other, BaseStrand):
            other = Strand(other)
        return self.int != other.int
    
    def __lt__(self, other):
        if not isinstance(other, BaseStrand):
            other = Strand(other)
        return self.int < other.int
    
    def __le__(self, other):
        if not isinstance(other, BaseStrand):
            other = Strand(other)
        return self.int <= other.int
    
    def __gt__(self, other):
        if not isinstance(other, BaseStrand):
            other = Strand(other)
        return self.int > other.int
    
    def __ge__(self, other):
        if not isinstance(other, BaseStrand):
            other = Strand(other)
        return self.int >= other.int
        
    def __mul__(self, other):
        if not isinstance(other, BaseStrand):
            other = Strand(other)
        return Strand(self.int * other.int)
    
    def __format__(self, spec):
        if spec and spec.endswith(('d','n')):
            return '{1:{0}}'.format(spec, self.int)
        return '{1:{0}}'.format(spec, self.str)

    def __index__(self):
        return self.int

    def __neg__(self):
        return self

    def __pos__(self):
        return self

    def __reversed__(self):
        return self.__neg__()
    
    def ispositive(self):
        return self.int > 0

    def isnegative(self):
        return self.int < 0

    def isunknown(self):
        return not (self.ispositive() or self.isnegative())
    
        
class PositiveStrand(BaseStrand):
    __slots__ = ()
    str = '+'
    int = +1
    def __neg__(self):
        return _STRAND[NegativeStrand.str]

    def __pos__(self):
        return self

        
class NegativeStrand(BaseStrand):
    __slots__ = ()
    str = '-'
    int = -1
    def __neg__(self):
        return _STRAND[PositiveStrand.str]

    def __pos__(self):
        return self

    
class UnknownStrand(BaseStrand):
    __slots__ = ()
    str = '.'
    int = 0
    
    
def register(newclass):
    if not issubclass(newclass, BaseStrand):
        raise TypeError("Strand class must inherit from BaseStrand")
    instance = newclass()
    instance_str = instance.str
    instance_int = instance.int
    if _math.isnan(instance_int):
        instance_int = _math.nan
    if instance_str in _STRAND:
        raise NameError("'%s' class exists" % instance_str)
    if instance_int in _STRAND:
        raise NameError("'%s' class exists" % instance_str)
    _STRAND[instance_str] = instance
    _STRAND[instance_int] = instance

    
def Strand(strand):
    try:
        if isinstance(strand, BaseStrand):
            return _STRAND[strand.str]
        elif isinstance(strand, (int, float)):
            if _math.isnan(strand):
                _strand = _math.nan
            else:
                _strand = (strand // abs(strand)) if strand else 0
            return _STRAND[_strand]
        elif isinstance(strand, str):
            return _STRAND[strand]
        else:
            raise TypeError("Unrecognized strand type (%s): '%s'" % (
                type(strand), str(strand)))
    except KeyError:
        raise ValueError("Unrecognized strand value: '%s'" % (str(strand)))
            

register(PositiveStrand)
register(NegativeStrand)
register(UnknownStrand)
