# strand

Installation:

```base
git clone https://github.com/bredeson/strand.git
cd strand
make install PREFIX=/path/to/installbase
```

## Usage:

```python
from strand import Strand
strand = Strand("+")
strand.int  # returns 1
strand = reversed(strand)
strand.int  # returns -1
print(strand.str)  # prints "-"
```

