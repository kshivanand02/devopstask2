# Node class representing each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList ADT
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Delete first node with given data
    def delete(self, key):
        current = self.head
        prev = None

        # If head node holds the key
        if current and current.data == key:
            self.head = current.next
            return

        # Search for the key
        while current and current.data != key:
            prev = current
            current = current.next

        # Key not found
        if not current:
            print(f"Key {key} not found in the list.")
            return

        # Unlink the node
        prev.next = current.next

    # Search for a node
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()  # Output: 10 -> 20 -> 30 -> None

    print("Searching for 20:", ll.search(20))  # Output: True
    print("Searching for 40:", ll.search(40))  # Output: False

    ll.delete(20)
    ll.display()  # Output: 10 -> 30 -> None

    ll.delete(40)  # Output: Key 40 not found in the list.
