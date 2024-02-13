import itertools
from dataclasses import dataclass, field
from heapq import heappush, heappop
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count()


def add_task(task, priority=0):
    """Add a new task or update the priority of an existing task"""
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    """Mark an existing task as REMOVED"""
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    """Remove and return the lowest priority task"""
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
        raise KeyError('pop from an empty priority queue')


add_task(1, 2)
print("priority queue after adding task:", pq)

add_task(2, 3)
add_task(3, 4)
add_task(4, 5)
print("Priority Queue after adding more tasks:", pq)

remove_task(2)
print('priority queue after removing task 2')

task = pop_task()
print("Popped task:", task)

