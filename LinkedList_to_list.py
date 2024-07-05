#linked List -> list
        if not head:
            return None

        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next

#list -> Linked List
        if not sums:
            return None
        
        # Initialize the new linked list
        new_head = ListNode(sums[0])
        current = new_head

        # Append remaining sums to the new linked list
        for value in sums[1:]:
            new_node = ListNode(value)
            current.next = new_node
            current = current.next
        
        return new_head
