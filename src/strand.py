

_STRAND = {}

class BaseStrand(object):
    @property
    def int(self):
        return self._int

    @property
    def str(self):
        return self._str
    
    def __str__(self):
        return self.str

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.str)
    
    def __eq__(self, other):
        return self.int == other.int
    
    def __ne__(self, other):
        return self.int != other.int
    
    def __lt__(self, other):
        return self.int < other.int
    
    def __le__(self, other):
        return self == other or self < other
    
    def __gt__(self, other):
        return self.int > other.int
    
    def __ge__(self, other):
        return self == other or self > other

    def __format__(self, spec):
        if spec == "" or spec[-1] == 's':
            return '{1:{0}}'.format(spec, self.str)
        else:
            return '{1:{0}}'.format(spec, self.int)

    def __reversed__(self):
        return self

    
class PositiveStrand(BaseStrand):
    _str = '+'
    _int = +1
    def __init__(self):
        self._int = PositiveStrand._int
        self._str = PositiveStrand._str

    def __reversed__(self):
        return _STRAND[NegativeStrand._str]
        
        
class NegativeStrand(BaseStrand):
    _str = '-'
    _int = -1
    def __init__(self):
        self._int = NegativeStrand._int
        self._str = NegativeStrand._str

    def __reversed__(self):
        return _STRAND[PositiveStrand._str]
    
    
class UnknownStrand(BaseStrand):
    _str = '.'
    _int = 0
    def __init__(self):
        self._int = UnknownStrand._int
        self._str = UnknownStrand._str
    
    
def register(newclass):
    if not issubclass(newclass, BaseStrand):
        raise TypeError("Strand class must inherit from BaseStrand")
    inst = newclass()
    if inst.str in _STRAND:
        raise NameError("%s class exists" % inst.str)
    _STRAND[inst.str] = inst
    if inst.int in _STRAND:
        return
    _STRAND[inst.int] = inst

    
def Strand(strand):
    try:
        if isinstance(strand, BaseStrand):
            return _STRAND[strand.str]
        elif isinstance(strand, (int, float)):
            _strand = (strand // abs(strand)) if strand else 0
            return _STRAND[_strand]
        else:
            return _STRAND[strand]
    except KeyError:
        raise ValueError("Invalid strand value: '%s'" % (str(strand)))
    except TypeError:
        raise TypeError("Invalid strand type (%s): '%s'" % (
            type(strand), str(strand)))
            

register(PositiveStrand)
register(NegativeStrand)
register(UnknownStrand)
