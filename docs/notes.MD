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
- Good for devide and conquer algorithms (as it is cheap to read everywhere).

**Cons**
- Arrays are expensive to add or remove in the middle.

## Lists
Require 2 primitive concepts:

1. **Pointers**, which give the reference to an address.
1. **Nodes**, which consists on at key (or value) and a pointer to a subsequent node.

Notice *Nodes* could also include pointers referencing their previous element.

Thus, a list consists on at least 
1. A **head** pointer, referencing the first element of the list (which could be `nil` for an empty list).
1. A **set of nodes**.

As mentioned, head pointer itself simply points to the *first* node of the list.

As we traverse each node, eventually we reach the *last* node, which pointer's is `nil` (it doesn't point to any subsequent element in the list).

Optionally, list could also have a **tail pointer** referencing their last element.

### **Singly-Liked Lists**

When each node implement only a pointer to their next element, we say we are working with a **Singly-Linked List**.

### **List API** (Singly-Linked List)
| Operation         | Description | Complexity (w.o. tail) | Complexity (with tail) |
| --                | -- | -- | -- |
| `PushFront(key)`  | add to front | `O(1)` | ~ |
| `TopFront()`      | return front item | `O(1)` | ~ |
| `PopFront()`      | return and remove front item | `O(1)` | ~ |
| `PushBack(key)`   | add to back | `O(n)` | `O(1)` |
| `TopBack()`       | return back item | `O(n)` | `O(1)` |
| `PopBack()`       | return and remove back item | `O(n)` | ~ |
| `Find(key)`       | assert element is in the list | `O(n)` | ~ |
| `Erase(key)`      | find and remove from the list | `O(n)` | ~ |
| `Empty()`     | assert if list is empty (head == nil) | `O(1)` | ~ |
| `AddBefore(node, key)` | adds key before node | `O(n)` | ~ |
| `AddAfter(node, key)` | adds key after node | `O(1)` | ~ |

### **Doubly-Linked List**
If we were to add in every node a pointer to the previous element, we would operate

### **List API** (Doubly-Linked List)
| Operation         | Description | Complexity (w.o. tail) | Complexity (with tail) |
| --                | -- | -- | -- |
| `PushFront(key)`  | add to front | `O(1)` | ~ |
| `TopFront()`      | return front item | `O(1)` | ~ |
| `PopFront()`      | return and remove front item | `O(1)` | ~ |
| `PushBack(key)`   | add to back | `O(n)` | `O(1)` |
| `TopBack()`       | return back item | `O(n)` | `O(1)` |
| `PopBack()`       | return and remove back item | `O(1)` | ~ |
| `Find(key)`       | assert element is in the list | `O(n)` | ~ |
| `Erase(key)`      | find and remove from the list | `O(n)` | ~ |
| `Empty()`     | assert if list is empty (head == nil) | `O(1)` | ~ |
| `AddBefore(node, key)` | adds key before node | `O(1)` | ~ |
| `AddAfter(node, key)` | adds key after node | `O(1)` | ~ |


**Pros**
- Constant time to insert at or remove from the front (in contrast to arrays).
- For doubly-linked lists it's also constant time to insert at or remove from the back.
- Elements need not be contigous.
- Elements need not be the same size.

**Cons**
- Bad for devide and conquer algorithms (as it is expensive to find elements in the middle of the list).
- Doubly linked list with head and tail require a bit more memory (yet provide write complexity advantages as mentioned).

## Stacks
Data type which follows **Last In First Out (LIFO)** conventions and satisfies the API shown below.

Before going further, it's worth mentioning stacks could be implemented using stacks or linked lists, thus we add the complexities respectively below.
### **Stack API**
| Operation | Description | Complexity (using array as base) | Complexity (using list as base) |
| -- | -- | -- | -- |
| `Push(key)` | add key to collection | `O(1)` if `\|stack\| <= \|array\|` else `O(n)` | `O(1)` |
| `Top()` | returns most-recently added key | `O(1)` | ~ |
| `Pop()` | returns and removes most-recently added key | `O(1)` | ~ |
| `Empty()` | assert if stack is empty | `O(1)` | ~ |

While list implementation has the overhead cost of including pointers, array has the overhead cost of reserving empty spaces.

## Queues
Data type which follows **First In First Out (FIFO)** conventions and satisfies the API shown below.

Similarly to stacks, *Queues* could be implemented both using a list or an array as base. However, we would need to use a **_circular array_** to preserve runtime complexity.

### **Queue API**
| Operation | Description | Complexity (using array as base) | Complexity (using list as base) |
| -- | -- | -- | -- |
| `Enqueue(key)` | add key to collection | `O(1)` if `\|queue\| <= \|array\|` else `O(n)` | `O(1)` |
| `Dequeue()` | removes and returns last-recently added key | `O(1)` | ~ |
| `Empty()` | assert if stack is empty | `O(1)` | ~ |

Same implementation overhead costs as with stacks apply for queues.
