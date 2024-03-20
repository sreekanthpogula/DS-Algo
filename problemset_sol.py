# Given a data structure D that supports Sequence operations:
# • D.build(X) in O(n) time, and
# • D.insert at(i, x) and D.delete at(i), each in O(log n) time,
# where n is the number of items stored in D at the time of the operation, describe algorithms to
# implement the following higher-level operations in terms of the provided lower-level operations.
# Each operation below should run in O(k log n) time. Recall, delete at returns the deleted item.
# (a) reverse(D, i, k): Reverse in D the order of the k items starting at index i (up to
# index i + k − 1). 
# (b) move(D, i, k, j): Move the k items in D starting at index i, in order, to be in front
# of the item at index j. Assume that expression i ≤ j < i + k is false. 


D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# reverse operation
def reverse(D, i, k):
    if k <= 2: 
        return
    x2 = D.delete_at(i + k - 1)  
    x1 = D.delete_at(i)
    D.insert_at(i, x2)
    D.insert_at(i + k - 1, x1)
    reverse(D, i + 1, k - 2)



# Move operations
def move(D, i, k, j):
    if k <= 1:
        return
    x = D.delete_at(i)
    if j > i:
        j = j - 1
    D.insert_at(j, x)
    j = j + 1
    i = i + 1
    move(D, i, k - 1, j)



