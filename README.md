# README

## Overview

This project contains a Python implementation of a **Queue** data structure using a **Singly-Linked List**. A queue is a linear data structure that operates on the **FIFO (First In, First Out)** principle, where elements are added to the back and removed from the front. 

The implementation includes two classes:
1. **Node**: Represents a single element in the queue.
2. **Queue**: Provides the functionality to manage the queue using the `Node` class.

---

## Classes and Methods

### 1. `Node`
A class representing a single node in the linked list.

#### Attributes:
- `data`: Stores the data for the node.
- `right`: A reference to the next node in the list.

### 2. `Queue`
A class implementing the queue structure using the Node class.
Attributes:
- first: Points to the first node in the queue.
- last: Points to the last node in the queue.
### How to Run the Program

```bash 
python queue.py
