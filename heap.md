Heap:

1. Heap is a tree - based data structure that satisfies heap property.
2. The heap is one maximally efficient implementation of an abstract data type called a priority queue.
3. A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority, or when insertions need to be interspersed with removals of the root node.
4. A common implementation of a heap is the binary heap, in which the tree is a complete binary tree.
5. When a heap is a complete binary tree, it has the smallest possible height—a heap with N nodes and a branches for each node always has loga N height.

Basic operations :
1. Finding maximum and minimum item of a max and min heap.  
2. Adding a new key (push). - O(1)
3. extracting max, min values from max, min heap after removing nodes (pop).
4. delete-max or min node after removing root node. O(1)
5. replacing - pop root and push a new key. This is more efficient than a pop followed by a push, since it only needs to balance once, not twice, and is appropriate for fixed-size heaps.

Creation: 
1. create-heap
2. heapify - O(1)
3. merge - preserving the two - heaps.
4. meld - joining two heaps two get new heap containing all the elements of both.

Inspection:
1. size
2. is-empty
3. increase, decrease - key
4. sift-up - move a node up in a tree
5. sift-down - move a node down in a tree

Applications:
1. Heapsort
2. finding max, min, median element in constant time.
3. graph algorithms - prims, Dijkstra's shortest-path.
4. priority queue