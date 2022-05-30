# Basics
We'll describe basic data structures and include details such as:
 - runtimes
 - memory usage
 - apis (methods)

To deepen the knowledge, we'll include some python or other programming language (C# or Java probably) implementations to be able to take advantage on the concepts.

## Arrays
1. Contiguous area of memory (either on the stack or heap)
1. Consists of equal size elements 
1. Such elements are indexed by contiguous integers.

Array has random access, which ensures **constant time access** (to *read or write*) to any particular element in an array.

In concrete, to find the address of an element in an array, the following *"formula"* can be applied to find the **i-th** index in an array:

```
arr[i]_addr := arr_addr + elem_size * (i - first_index)
```
(thus, we compute the in-memory address of any item in *O(1)*)

*Example declaration*

**1.**
```
# arr_length to be a variable of type int that corresponds to the array length
arr = [None] * arr_length
```

**2.**
```
import array as arr
# the first parameter correspond to the type of items we can store in the array
my_arr = arr.array('i', [1,2,3])
```
The following types are supported by the python array.array class:

| type code | C type         | Python Type  | Minimum size in bytes |
| --        | --             | --           | --:       |
| `'b'`     | signed char    | int          | 1         |
| `'B'`     | unsigned char  | int          | 1         |
| `'u'`     | wchar_t        | unicode char | 2         |
| `'h'`     | signed short   | int          | 2         |
| `'H'`     | unsigned short | int          | 2         |
| `'i'`     | signed int     | int          | 2         |
| `'I'`     | unsigned int   | int          | 2         |
| `'l'`     | signed long    | int          | 4         |
| `'L'`     | unsigned long  | int          | 4         |
| `'q'`     | signed long long | int        | 8         |
| `'Q'`     | unsigned long long | int      | 8         |
| `'f'`     | float          | float        | 4         |
| `'d'`     | double         | float        | 8         |

### **Multi-dimensional arrays**
Follow the same principles of an array.

#### *Layouts*
There are 2 ways we can layout multi-dimensional arrays.

1. **Row major**: where we walk first over a given row.
    - Column indexes change more rapidly.
    - `(1, 1), (1, 2), ..., (1, n), (2, 1), (2, 2), ..., (2, n), ...`
1. **Column major**: we walk first over a given columns
    - Row indexes change more rapidly
    - `(1, 1), (2, 1), ..., (m, 1), (1, 2), (2, 2), ..., (m, 2), ...`

### **Array operations**
|               | Add    | Remove |
| --            | ---    | ------ |
| **Beginning** | `O(n)` | `O(n)` |
| **End**       | `O(1)` | `O(1)` |
| **Middle**    | `O(n)` | `O(n)` |


**Pros**
- Arrays are great if you want to add or remove at the end.
- Read or write anywhere in constant time.

**Cons**
- Arrays are expensive to add or remove in the middle.

## Singly Liked Lists
