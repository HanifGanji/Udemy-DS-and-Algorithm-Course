from src.linked_list.SLL import SingleLinkedList


if __name__ == "__main__":

    sll = SingleLinkedList()

    for location in range(1, 4):
        sll.insert(value=f"node_{location}", location=location)
    sll.print_linked_list()

    sll.insert("node_4", 4)
    sll.print_linked_list()

    sll.insert("new_node_4", 4)
    sll.print_linked_list()

    sll.insert("new_head", 1)
    sll.print_linked_list()
