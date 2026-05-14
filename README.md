# Name

`strand` - Python module providing a strand object API

# Description

The `strand` module  provides classes for handling the three most common strand
forms -- positive (`+`), negative (`-`), and unknown (`.`) -- as both string
and integer types.

# Installation:

```base
git clone https://github.com/bredeson/strand.git
cd strand
make install PREFIX=/path/to/install/prefix
```

# Documentation:

After proper installation, there are two ways of getting the complete documentation for the `strand` API. Read `man`-like help pages by doing either of the following:

1. On the command line:
    ```bash
    $ pydoc strand
    ```

2. In the Python REPL:
    ```python
    >>> import strand
    
    >>> help(strand)
    ```

# Examples:

In the Python REPL:

```python
>>> from strand import Strand

>>> strand = Strand("+")
>>> strand.ispositive()
True
>>> strand.int
1
>>> strand = reversed(strand)
>>> strand.isnegative()
True
>>> strand.int
-1
>>> print(strand)  # prints "-"
```

