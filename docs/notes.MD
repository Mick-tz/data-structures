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
(thus, we compute the in-memory address of any item in $O(1)$)

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
| **Beginning** | $O(n)$ | $O(n)$ |
| **End**       | $O(1)$ | $O(1)$ |
| **Middle**    | $O(n)$ | $O(n)$ |


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
| `PushFront(key)`  | add to front | $O(1)$ | ~ |
| `TopFront()`      | return front item | $O(1)$ | ~ |
| `PopFront()`      | return and remove front item | $O(1)$ | ~ |
| `PushBack(key)`   | add to back | $O(n)$ | $O(1)$ |
| `TopBack()`       | return back item | $O(n)$ | $O(1)$ |
| `PopBack()`       | return and remove back item | $O(n)$ | ~ |
| `Find(key)`       | assert element is in the list | $O(n)$ | ~ |
| `Erase(key)`      | find and remove from the list | $O(n)$ | ~ |
| `Empty()`     | assert if list is empty (head == nil) | $O(1)$ | ~ |
| `AddBefore(node, key)` | adds key before node | $O(n)$ | ~ |
| `AddAfter(node, key)` | adds key after node | $O(1)$ | ~ |

### **Doubly-Linked List**
If we were to add in every node a pointer to the previous element, we would operate

### **List API** (Doubly-Linked List)
| Operation         | Description | Complexity (w.o. tail) | Complexity (with tail) |
| --                | -- | -- | -- |
| `PushFront(key)`  | add to front | $O(1)$ | ~ |
| `TopFront()`      | return front item | $O(1)$ | ~ |
| `PopFront()`      | return and remove front item | $O(1)$ | ~ |
| `PushBack(key)`   | add to back | $O(n)$ | $O(1)$ |
| `TopBack()`       | return back item | $O(n)$ | $O(1)$ |
| `PopBack()`       | return and remove back item | $O(1)$ | ~ |
| `Find(key)`       | assert element is in the list | $O(n)$ | ~ |
| `Erase(key)`      | find and remove from the list | $O(n)$ | ~ |
| `Empty()`     | assert if list is empty (head == nil) | $O(1)$ | ~ |
| `AddBefore(node, key)` | adds key before node | $O(1)$ | ~ |
| `AddAfter(node, key)` | adds key after node | $O(1)$ | ~ |


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
| `Push(key)` | add key to collection | $O(1)$ if $\|stack\| \leq \|array\|$ else $O(n)$ | $O(1)$ |
| `Top()` | returns most-recently added key | $O(1)$ | ~ |
| `Pop()` | returns and removes most-recently added key | $O(1)$ | ~ |
| `Empty()` | assert if stack is empty | $O(1)$ | ~ |

While list implementation has the overhead cost of including pointers, array has the overhead cost of reserving empty spaces.

### Example Usage
A typical usage for Stacks is keeping track of symmetrical operations.  
As an example, we can use Stacks to keep track whether parenthesis or brackets are being used consistently in a text.

Python example:
```Python
LEFT_VALUES = ["[", "("]
RIGHT_VALUES = ["]", ")"]
COMPANIONS = {
  "]": "[",
  ")": "(",
}
def is_balanced(text: str):
  stack = Stack()
  for char in text:
    if char in LEFT_VALUES:
      stack.push(char)
    if char in RIGHT_VALUES:
      if stack.is_empty():
        return False
      if (COMPANIONS.get(char, None) != stack.pop()):
        return False
  return stack.is_empty()
```

In the previous example, we assume we have implemented an explicit Stack class. We naturally can simply use a python `list` or a `deque` (from `collections` package). `deque` implementation is typically preferred as it proviedes $O(1)$ complexity while pushing and popping (in contrast to list's $O(n)$ complexities).

In python is third option to use the `queue` from `LifoQueue` package. In the back, this implementation will require you to provide a `maxsize`. 

Notice that another name for _Stacks_ is _LIFOQueues_ as shown in the python module.


## Queues
Data type which follows **First In First Out (FIFO)** conventions and satisfies the API shown below.

Similarly to stacks, *Queues* could be implemented both using a list or an array as base. However, we would need to use a **_circular array_** to preserve runtime complexity.

### **Queue API**
| Operation | Description | Complexity (using array as base) | Complexity (using list as base) |
| -- | -- | -- | -- |
| `Enqueue(key)` | add key to collection | $O(1)$ if `\|queue\| <= \|array\|` else $O(n)$ | $O(1)$ |
| `Dequeue()` | removes and returns last-recently added key | $O(1)$ | ~ |
| `Empty()` | assert if stack is empty | $O(1)$ | ~ |

Same implementation overhead costs as with stacks apply for queues.

## Trees
Trees are defined recursively as follows:

1. `Empty`, or
1. A `Node` that contains
    - a `key` (or value)
    - a `list of child trees`

A tree defines a hierarchy where nodes included in the list of child tree of a give node are considered to be below in the hierarchy. 

The *topmost Node on a tree* is known as the **root** of the tree.  

An **ancestor** (from a given node) is a node that lies above in the hierechy and **child node** is one that stays one positiion below in the hierachy (from the considered *parent*). We considere an **edge** to connect a *parent node* with it's *children*. 

A **descendant** is the inverse concept than an ancestor.

*Nodes* sharing the same parent are considered **siblings**.

A **leaf** is a node that has no children. Conversely, an **interior node** is a node having children that isn't the root.

The **level** of a *node* is 1 plus the number of *edges* that need to be traversed to reach the *root* (thus, the level of the *root node* is 1). Similarly, **level n+1** is the set of nodes which are *n edges away from the root node*.

The **height** of a node is the maximum depth of a subtree node in it's child's list.

A **Forest** is a *collection of trees* (having different roots).

When we implement a tree, we could add a (optional) reference to the parent of any given node, making it simpler to traverse the tree up and downwards.

### **Binary Trees**
Trees in which each node has at most 2 children are known as binary trees and are of particular interest as they are really useful.

*Node* implementations of binary trees tend to have explicit definitions for left and right children rather than implementing them as a list of childs.

### **Tree traversals**
Often we want to visit the nodes of a tree in a particular order.

There are 2 main ways of traversing a tree:
  1. **Depth-first**: we completely traverse one sub-tree before exploring any siblings.
  1. **Breadth-first**: we completely traverse all nodes at one level before progressing to the next level.

### **Depth-First**
Binary trees can easily be traversed taking advantage of a derived total ordering of the tree. Such recursive algorithm is usually known as *in order traversal*.
```python
class BinaryTree:
  ...
  def in_order_traversal(self, func):
    """
    apply func to every key in the tree, traversing all elements in a branch before moving to the next
    """
    if self.is_empty():
      return
    self.left_child.in_order_traversal()
    func(self.key)
    self.right_child.in_order_traversal()
  ...
```

This idea can be generalized to non-binary trees by simply changing the moment we call `func` over the current node key. Such algorithms are known as *pre order traversal* and *post order traversal*, respectively.

```python
class Tree:
  ...
  def pre_order_traversal(self, func):
    """
    apply func to every key in the tree, traversing all elements in a branch before moving to the next
    """
    if self.is_empty():
      return
    func(self.key)
    for child_tree in self.child_trees
      child_tree.pre_order_traversal()


  def post_order_traversal(self, func):
    """
    apply func to every key in the tree, traversing all elements in a branch before moving to the next
    """
    if self.is_empty():
      return
    for child_tree in self.child_trees
      child_tree.post_order_traversal()
    func(self.key)
  ...
```

**_OBS:_** An important, inconspicuous, detail of these algorithms, is that they discreetly utilize a stack under the covers as a mean to keep track of where we are at any given point of the execution.

### **Breadth-First**
We illustrate the algorithm in binary trees as it's easier to understand, yet it would not be hard to generalize it to general trees.
```python
class BinaryTree:
  ...
  def level_traversal(self, func):
    """
    apply func to every key in the tree, traversing all elements in a level before moving to the next
    """
    if self.is_empty():
      return
    pending_queue = Queue()
    pending_queue.enqueue(self)
    while not pending_queue.is_empty():
      node = pending_queue.dequeue()
      func(node.key)
      if node.left_child:
        pending_queue.enqueue(node.left_child)
      if node.right_child:
        pending_queue.enqueue(node.right_child)

  ...
```

**_OBS:_** Conversely to what we have mentioned before, breadth first (search) algorightms take advantage of queues. 

## Indirection
Rather than directly storing our reference to the static of dynamically allocated chunk of memory, we store a pointer to that chunk of memory.
## Dynamic Arrays
*Dynamic arrays* are also known as rizesable arrays.

They differ to *dynamically allocated arrays* which are simply arrays who's size is determined at run time, but never changes.

They allow us to dynamically increase the size of an array, by storing a pointer to a given dynamically allocated array, and replace it with a newly allocated array as needed (by the size constraints).

### **Dynamic arrays API**
| Operation   | Description                     | Complexity |
| --          | --                              | --         |
| `Get(i)`    | returns element at location `i` | $O(1)$     |
| `Set(i, v)` | sets element `i` to value `v`   | $O(1)$     |
| `PushBack(v)` | adds value `v` at the end     | $O(1)^*$     |
| `Remove(i)` | removes element at location `i` | $O(n)$     |
| `Size()`    | returns the number of elements  | $O(1)$     |

\* *`PushBack(v)` is $O(n)$ for the worst case scenario. However, doing amortized analysis, we find it to be $O(1)$ almost everywhere.*

### Implementation
In order to implement dynamical arrays we require 3 components:
  1. *arr*: dynamically-allocated array
  1. *capacity*: size of *arr*
  1. *size*: number of elements currently in *arr*

**_OBS:_** All of the following are actually implementations of *dynamic arrays*

  - C++: vector
  - Java: ArrayList
  - Python: list

## Amortized Analysis
When calculating complexity for certain algorithms, we find examples where looking at the individual worst-case scenario may be too severe.

Alternatively, it might be that we are looking for the *total worst-case cost* for a sequence of operations, some of which are expensive and some of which aren't.

We define the **Amortized cost** of a given sequence of *n* operations as:

```python
# cost(ops) is the set of costs of all the operations 
amortized_cost = sum(cost(ops)) / len(ops)
```

### Aggregate Method (for amortized analysis)
The *aggregate method* for calculating amortized analysis consists simply on using the defintion as state above in order to get the amortized cost of an algorithm.

To examplify, we use the *aggregate method* to calculate the amortized cost of dynamic array's `PushBack(v)` method

```python
def is_power_of_two(n: int) -> bool:
  """returns whether a number is a power of 2 """
  pass

costs = []
for i in range(n):
  cost = i + (i - 1) if is_power_of_two(i - 1) else 1
  costs.append(cost)
cost = sum(costs) / n
```
In this case, as `n` grows, `sum(costs)` will tend to `n`.

### Banker's Method (for amortized analysis)
The intuition of the *banker's method* is that we'll follow the next steps:
  1. We'll "charge extra" for each cheap operation.
  1. The "extra charge" is saved as tokens (conceptually).
  1. We use the saved tokens to "pay" for expensive operations.

Notice that the "extra charge" depend on the algorithm that we have in hand. But the idea is save enough "extra tokens" so that when we have to perform an expensive operation, we can fulfill the cost with the prepaid tokens.

To exemplify, let us discuss the cost of `PushBack(v)` using this idea.

If we consider every `PushBack(v)` call to take 3 operations (`O(3)=O(1)`), we can calculate cost as follows (we start with an existing array of size 4 where 2 values where already inserted):

  1. Adding a 3th element costs 3 (1 is for the actual insert, we save 1 for moving the 1st element and one for moving the 3th element).
  1. Adding a 4th element costs 3 (1 is for the actual insert, we save 1 for moving the 2nd element and one for moving the 4th element).
  1. When we intend to Push again, we need to resize the array (as it is already filled), we create the new array (size 8), and we move the 4 elements which we already have (we have enough tokens to move them at cost 0), finally, we push to this new copy of the array at cost 3 (1 is for the actual insert, we save 1 for moving the 1st element and one for moving the 5th element).
  1. This pattern repeats itself.

As we can see, we have "showned" (with some things to detail) that `PushBack(v)` has a complexity $O(3)=O(1)$.

### Physiscist Method (for amortized analysis)
In *pysicist method* (for amortized analysis), we define an potential function, `phi`, which maps states of the data structure to integers.

Such a function should satisfy the following:
  - `phi(h0) = 0 # where h0 is the initial state of the data structure` 
  - `0 <= pho(hn)`

Finally, we calculate amortized cost with the following formula:
```python
# t = j + 1
ac_t = c_t + phi(h_t) - phi(h_j)
```
Where `c_t` is the true cost of an operation (in the `PushBack(v)` example, `c_t = 1`).

Thus, we choose `phi` in such a way that, when `c_t` is small, the potential increases and conversely, the potential decreases when `c_t is large`.

Notice that the sum of these costs has the sum of the actual costas as a lower bound (thus, it makes sense to use this calculation)
```python
# truly phi(h_n) - phi(h_0) + sum(costs), but phi(h_0) = 0
amortize_cost = phi(h_n) + sum(ac_costs)
```

To exemplify, we can define `phi(h) = 2 * (size - capacity)` for the amortized analysis of the `PushBack(v)` method.

## Priority Queues
*Priority Queues* are a generalization of the standard Queue data structure in which each element is assigned a priority and elements come out in order of priorities.

*Priority Queues* are typically used for scheduling jobs.

### Priority Queues API
| Operation   | Description               | Complexity (using heaps) |
| --          | --                                      |  --        |
| `Insert(p)` | Adds new element with priority `p`      | $O (tree\ height)^*$ |
| `ExtractMax`| Extracts the element with max priority  | $O (tree\ height)^*$ |
| `Remove(it)`| Removes an element pointed by iterator `it`| $O (tree\ height)^*$ |
| `GetMax`| Returns element with max priority w.o. removing it | $O(1)$ |
| `ChangePriority(it,p)`| Using iterator `it` updates priority to `p` | $O (tree\ height)^*$ |

*We'll see we can manage to have $O (tree\ height)=O (\log n)$
### Algorithms and built-in implementations

The following algorithms use priority queues
  - Dijsktra: finding shortest path in a graph 
  - Prim: construct graph with minimum spanning tree of a graph
  - Huffman: construct optimum prefix-free encoding of a string
  - Heap sort: sorting a sequence

The following are famous built-in implementations of priority queues:
  - C++: priority_queue
  - Java: PriorityQueue
  - Python: heapq

Notice in python, we use a heap to implement priority queues. This is give to the fact that priority queues rely on primitive data structures, like arrays or lists, to be implemented. However, naively using either of those (arrays or lists) will yield inefficient implementations of the priority (either `Insert(p)` or `ExtractMax` would execute in linear time).

## Binary Heap
A *Binary max-heap* is a binary tree, where the value of each node is at least the value of its children.

In other words, the ordering in the tree corresponding to the (total) ordering of the values in its nodes (each parent nodes value, is greater than or equal the values of its children nodes).

### Complete Binary heaps
When we use a binary heap as the underlying structure of a priority queue, we want to keep the tree *as shallow as possible* since most operations will have complesity $O(tree\ height)$.

In order to achieve this property, a natural approach is to require that all levels are fully packed. This notion is known as a *complete tree*.

In concrete, we say that a *binary tree is complete* if all its levels are filled, except possibly for the deepest one which is filled from left to right.

**_OBS_**: A complete binary tree with $n$ nodes has height at most $O(\log n)$.

An additional advantage of binary complete trees as binary heaps, is that they can be implemented using an array, when we start enumerating from the maximum node and follow up from left to right.

In such a case, we can get the values in each element by using the following formulas

```python
# i represent the number of the node, e.g. topmost node is 1
parent(i) = i // 2 # floor(float(i)/2.0)
leftchild(i) = 2 * i
rightchild(i) = 2 * i + 1
```

### Trade offs
The trade off of using complete binary trees is that we must ensure that the tree remains complete at any point.

Concretely, both `Insert(p)` and `ExtractMax` change the shape of a tree, and thus we need to be extra careful in order to define them as to not lose completeness.

`Insert(p)` can be easily implemented, simply by assuring we add a node to the leftmost vacant spot at the bottom level.

Similarly, to `ExtractMax`, we simply swap the max with the last node and perform siftdown accordingly.

### Heap Sort
One important algorithm that relies on heaps is the *heap sort algorithm*, which is both a fast and efficient sorting algorithm.

The algorithm is quite straightforward (and a generalization of selection sort) and thus we describe it below.

```
HeapSort(A[1...n])
  priorityQueue <- new PriorityQueue
  for i from 1 to n:
    priorityQueue.Insert(A[i])
  for i from n down to 1:
    A[i] <- priorityQueue.ExtractMax()
```

Complexity of heap sort is $O(n\log n)$, since  both `Insert` and `ExtractMax` work in logarithmic time for complete binary heaps.

As mentioned, heap sort is a generalization of selection sort, in which instead of finding naively the maximum value at each iteration, we use a smart data structure.

The *Trade Off* of using heap sort over selection sort is that is uses additional spaces to store the priority queue.

### Some implementations
Turning an array into a heap is quite simple, thus we describe it below

```python
def sift_down(arr, size, root) -> None:
  largest = root # naively set root as largest
  left = 2 * root + 1 # left child index
  right = 2 * root + 2 # right child index

  # left child larger than root
  if (left < size and arr[largest] < arr[left]):
    largest = left
  
  # right child is larger than largest so far
  if right < size and arr[largest] < arr[right]:
    largest = right
  
  # correctly set largest value as root
  if largest != root:
    arr[root], arr[largest] = arr[largest], arr[root]

    # recursively sift_down sub tree
    sift_down(arr, size, largest)


def heapify(arr):
  size = len(arr)
  # we start from floor(size/2) - 1 as leafs are heaps
  for i in range(size // 2 - 1, -1, -1):
    sift_down(arr, size, i)
```
Python already has an in-built component for it in the standard library `heapq` module.

**However**, only min-heaps are currently supported, even tho private functions exist (currently) for max-heaps as shown below. 

```python
import heapq

example_arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
# from previous implementation
heapify(example_arr)
print(example_arr)
# [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]

example_arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
heapq._heapify_max(example_arr)
print(example_arr)
# [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
```
Finally, using our implementation of the *max-heap*, we can easily implement heap sort as shown below.

```python
import sys
from array import array


class MaxHeap:
  def heapify(self, arr) -> None:
    # as defined above
    ...

  def sift_down(self, arr, size, root) -> None:
    # as defined above
    ...

  def heap_sort(self, arr):
    size = len(arr) - 1
    self.heapify(arr)
    for i in range(size):
      # first element is current maximum
      arr[0], arr[size - i] = arr[size - i], arr[0]
      # sift down (almost always) incorrect first element
      self.sift_down(arr, size - i - 1, 0)


if __name__ == "__main__":
  arr = array('i', [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17])
  max_heap = MaxHeap()
  max_heap.heap_sort(arr)
  sys.stdout.write(f"{str(arr)}\n")
  # array('i', [1, 3, 4, 5, 6, 8, 9, 10, 13, 15, 17])
```

### Trade Offs
*Heap sort* is usually compared to quicksort with the following highlights:

**Heap sort:**
  - In place, i.e. no extra memory required to sort
  - Worst case $O(n\log n)$

**Quick sort:**
  - Faster than heap sort
  - Average case $O(n\log n)$

Because of this, a common approach known as *Intra sort* is sometimes used.

i.e.
  - Run *Quicksort* algorithm
  - Keep track of recursion depth
  - If recursion depth exceeds $c\cdot\log n$ for some constant $c$:
    - stop *quicksort*
    - switch to *heapsort*

### Partial sorting
Finally, we have to mention that heaps are really efficient when we want to partially sort an array, i.e. when we want to obtain the $k$ largest or smalles elements in an array.

This comes from the fact that *heapifying* an array has complexity $O(n)$, thus, finding the $k$ largest (or smallest) elements form an array can be performed in linear time when $k = O\big(\frac{n}{\log n}\big)$.

The algorithm to do this is quite simple as shown below:
```
PartialSorting(A[1...n], k):
  BuildHeap(A)
  for i from 1 to k:
    ExtractMax()
```
which will of course have runtime $O(n + k\cdot\log n)$.

In python, `heapq` module provides this functionality natively
```python
import heapq

arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(arr) # O(n)

# 2 largest
heapq.nlargest(2, arr)
# 2 smallest
heapq.nsmallest(2, arr)
```
### Min-heaps
We mention min-heaps before, thus, we quickly define them formally to round up the section

A **_Binary min-heap_** is a binary tree where the value of each node is at most the value of its children.

This is of course useful for when we want to access elements with minimum priority in each case.

## Disjoint Sets
*Disjoint Sets* are collections of items in which we don't have repetition and each collection is disjoint to any other different collection. To put it in another way, disjoint sets are a way to partition a collection of data. We assign to each set a unique id, which we use to map it's items into that id.

I order to implement *disjoint sets* efficiently, trees are commonly used as follows:

 - each set is represented as a rooted tree
 - each node value is an integer `i`
 - such integers must be consecutives
 - id of a set is the root of the tree
 - we use an array `parent[i...n]` where we store the parent of each node, concretely `parent[j]` is the parent of node `j` or `j` in case `j` is the root

### Disjoint Sets API
| Operation   | Description               | Complexity  |
| --          | --                                      |  --        |
| `MakeSet(i)` | Creates a set containing `i`  | $O(1)$ |
| `Find(i)`| Finds id of set that contains `i` | $O(\log n)$ |
| `Union(i,j)`| Merges sets containing `i` and `j` | $O(\log n)$ |

We show an example implementation to achieve this complexity using an heuristic called *rank heuristic*, where we store a `ranks` array, containg the heights of each subtree
```python
from array import array
class DisjointSet:
  def __init__(self, n: int):
    self._parents = array('i', range(n))
    self._ranks = array('i', [0]*n)

  def make_set(self, i: int) -> None:
    self._parents[i] = i
    self._ranks[i] = 0

  def find(self, i: int) -> int:
    while i != self._parents[i]:
      i = self._parents[i]
    return i

  def union(self, i, j) -> None:
    i_set_id = self.find(i)
    j_set_id = self.find(j)
    if i_set_id == j_set_id:
      return
    if self._ranks[j_set_id] < self._ranks[i_set_id]:
      self._parents[j_set_id] = i_set_id
    else:
      self._parents[i_set_id] = j_set_id
      self._ranks[j_set_id] += int(self._ranks[j_set_id] == self._ranks[i_set_id])
```
There is a way to improve this algorithm using a heuristic known as *path compression*. To do so, we just need to adjust our find operation in order not to lose information of a root node while calling it, as shown below

```python
class DisjointSet:
...
  def find(self, i):
    if i != self._parents[i]:
      self._parents[i] == self.find(self._parents[i])
    return self._parents[i]
...
```

Notice that, when using *path compression* (in our current implementation), `ranks[i]` is no longer equal to the height of the subtree rooted as `i`. This is due to the fact that `find` will not change values related to the rank, yet it will *flatten* the tree. Nonetheless `ranks[i]` is still an upper bound for the height of the subtree rooted at `i`

>**_Def:_** The **_iterated logarithm_** of $n$, denoted by $\log^*(n)$, is the number of times the logarithmic function needs to be applied to $n$ before the result is less or equal than 1.

It is not hard to proof that the *amortized running time* of each operation, using our implementatino is $O(\log^*(n))$ (which could be considered to be constant for practical values of $n$ as $\log^*(2^{65536}) = 5$)

## Hashing
>**_Def:_** For any set of objects $S$ and any integer $m\in\omega\setminus 1$, a function $h: S\to m$ is called a **_hash function_**. In other words, a **_hash function_** is a function that maps the set *S* into a set of non-negative integers.

>**_Def:_** In the context of the previous definition, we call $m$, the cardinality of $h$.

The expectations on hash functions to be useful is that:
  - they should be fast to compute
  - should be *injective*
  - direct adressing using $O(m)$ memory
  - thus, $m$ is expected to be relatively small
  
>**_Def:_** When $h(o_1)\ne h(o_2)$ and $o_1\ne o_2$ (i.e. $h$ is not *one to one*), we will call this event a **_collision_**.

So in general, when we cannot guarentee our hash function to be injective, we still hope it has a small probability of collisions.

### Chaining
Unsurprisingly, we tend to use hash functions alongside arrays to store and efficiently retrieve related data.

In the case where we found a hash function satisfying the aformentioned constraints, we would still have to define how we would treat *collisions* in order not to lose data.

This is where **_chaining_** comes handy, basically, it consists in using arrays that maps to lists, thus when a collision occurs, instead of losing any information, we would just append the new information to the list which is stored in our array (and accessed using the integer we obtained from hashing as an index).
## Maps
A **_Map from set S into set V_** is a data structure that allows you to store a set of keys (elements of *S*) that maps into different values (which are elements of *V*).

### Maps API
| Operation   | Description               | Complexity  |
| --          | --                             |  --    |
| `HasKey(k)` | Checks whether `k` is a key    | $\Theta(c + 1)^*$ |
| `Get(k)`| Return the value associated to `k` | $\Theta(c + 1)^*$ |
| `Set(k,v)`| Associates value `v` to key `k`  | $\Theta(c + 1)^*$ |

*Where $c$ is the length of the longest chain.

**_Obs:_** If $n$ is the number of different objects currently in the map and $m$ is the cardinality of the hash function, then the memory consumption for chaining is $\Theta(n + m)$.

Thus, we want to find ways (and a good hash function is vital for this) to assert that both $m$ and $c$ are as small as possible to have a good performance.
## Sets
A **_set_** is a data structure that allows us to store elements without repetetion (same concepts as we explored with disjoints sets, but we won't be policing to partition an original collection).

### Sets API
| Operation   | Description               | Complexity  |
| --          | --                             |  --    |
| `Add(o)`   | include object `o` in the set   | $\Theta(c + 1)^*$ |
| `Remove(o)`| fromove object `o` from the set | $\Theta(c + 1)^*$ |
| `Find(o)`  | check if `o` is in the set      | $\Theta(c + 1)^*$ |

Objects are typically implemented using chaining, thus the complexities remain the same.

## Hash Tables
Finally, hash tables are implementations of either a Map or a Set where we use a hash function to map our objects (keys) into our values.+

Notice the definition for this data structure didn't actually required the usage of hash functions, although we have been assuming for some of our calculations they are implemented in such a way.

### Some implementations
Set:
  - `HashSet` in Java
  - `set` in python
Map:
  - `HashMap` in Java
  - `dict` in python
