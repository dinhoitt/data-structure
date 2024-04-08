class ListNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy')
        self.__numItems = 0

    def insert(self, i, newItem):
        if i < 0 or i > self.__numItems:
            return False  

        # Handle the case when inserting at the beginning separately
        if i == 0:
            prevNode = self.__head
        else:
            # Find the previous node (one position before where the new item will go).
            prevNode = self.getNode(i - 1)
        
        # This check is to ensure prevNode is not None
        if prevNode is None:
            return False

        # Create a new node and link it to the next node.
        newNode = ListNode(newItem, prevNode.next)
        # Update the previous node to point to the new node.
        prevNode.next = newNode
        # Increment the count of items in the list.
        self.__numItems += 1
        return True

    def getNode(self, i: int) -> ListNode:
        if i >= self.__numItems or i < 0:
            return None  # Alternatively, raise an exception.

        curr = self.__head
        for index in range(i + 1):
            curr = curr.next
        return curr

def mergeAndSortLists(list1, list2):
    mergedList = LinkedListBasic()
    current1, current2 = list1.getNode(0), list2.getNode(0)
    
    while current1 is not None and current1.item != 'dummy' or current2 is not None and current2.item != 'dummy':
        if current1 is None or current1.item == 'dummy' or (current2 is not None and current2.item != 'dummy' and current2.item < current1.item):
            item = current2.item
            current2 = current2.next
        else:
            item = current1.item
            current1 = current1.next

        # Find the position to insert the item in the merged list
        position = 0
        currentNode = mergedList.getNode(position)
        while currentNode and currentNode.item != 'dummy' and currentNode.item <= item:
            position += 1
            currentNode = mergedList.getNode(position)
        
        mergedList.insert(position, item)
    
    return mergedList

def populate_linked_list(linked_list, values):
    for i, value in enumerate(values):
        linked_list.insert(i, value)

# Initialize list1 and list2 as instances of LinkedListBasic
list1 = LinkedListBasic()
list2 = LinkedListBasic()

# Populate list1 and list2 with their respective values
populate_linked_list(list1, [1, 1, 2, 5])
populate_linked_list(list2, [1, 2, 3, 4])

# Merge and sort list1 and list2
mergedList = mergeAndSortLists(list1, list2)

# Function to print the items of a linked list for verification
def print_linked_list(linked_list):
    items = []
    current = linked_list.getNode(0)
    while current is not None and current.item != 'dummy':  # Adjusted condition
        items.append(current.item)
        current = current.next
    return items

# Print merged list for verification
print(print_linked_list(mergedList))
