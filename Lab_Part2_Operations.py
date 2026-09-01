# Lab ระหว่างเรียน ส่วนที่ 2: การดำเนินการกับลิสต์ (Operations)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next

    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue


def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


def deleteSpecificNode(head, nodeToDelete):
    if head is None or nodeToDelete is None:
        return head

    if head == nodeToDelete:
        return head.next

    previousNode = None
    currentNode = head

    while currentNode is not None and currentNode != nodeToDelete:
        previousNode = currentNode
        currentNode = currentNode.next

    if currentNode is None:
        return head

    previousNode.next = currentNode.next
    return head


print("--- ผลลัพธ์ส่วนที่ 2: Operations ---")

node1 = Node(9)
node2 = Node(1)
node3 = Node(7)
node4 = Node(8)
node5 = Node(13)

node1.next = node2
node2.next = node3
node3.next = node4

