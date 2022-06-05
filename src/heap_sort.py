import sys
from array import array

class MaxHeap:
  def heapify(self, arr) -> None:
    size = len(arr)
    # we start from floor(size/2) - 1 as leafs are heaps
    for i in range(size // 2 - 1, -1, -1):
      self.sift_down(arr, size, i)


  def sift_down(self, arr, size, root) -> None:
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
      self.sift_down(arr, size, largest)


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
  sys.stdout.write(str(arr))
  sys.stdout.write("\n")