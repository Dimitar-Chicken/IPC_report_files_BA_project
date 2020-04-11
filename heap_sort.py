import timeit
import random

def heapify(numbers, heap_size, root_index):

    # Assigns the index to be the largest element.
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index and the element is greater
    # than the current largest element, update the largest element.
    if left_child < heap_size and numbers[left_child] > numbers[largest]:
        largest = left_child

    # If the right child of the rood is a valid index and the element is
    # greater than the current largest element, update the largest element.
    if right_child < heap_size and numbers[right_child] > numbers[largest]:
        largest = right_child

    # If the largest element is not the root, perform a swap to move
    # the new largest element to be the root.
    if largest != root_index:
        numbers[root_index], numbers[largest] = numbers[largest], \
        numbers[root_index]
        # Recursively perform the operation to ensure the largest element
        # of the array becomes the root.
        heapify(numbers, heap_size, largest)


def heap_sort(numbers):
    
    n = len(numbers)

    # Iterates over the length of the given numbers array.
    # The two arguments following the length make the iteration go backwards
    # and make it so it stops at the second element of the array.
    for i in range(n, -1, -1):
        heapify(numbers, n, i)

    # Iterates over one shorter of the length of the given numbers array.
    # Iteration is backwards and stops at the first element of the array.
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)


random_list_of_numbers = random.sample(range(1, 5001), 5000)
print("List length: {}\n".format(len(random_list_of_numbers)))
word_paste = []
runs = 30
current = 0
average = 0.0

while current < runs:
    setup = ("from __main__ import heap_sort;"
             "random_list_of_numbers = {}".format(random_list_of_numbers))
    run_result = timeit.timeit(stmt="heap_sort(random_list_of_numbers)",
                               setup=setup, number=1)
    word_paste.append(round(run_result, 6))
    print("Run {}: {}".format(current + 1, run_result))
    average = average + run_result
    current = current + 1

print("\nAverage: {}".format(average/runs))

print("\nWord paste:")
for i in range(len(word_paste)):
    print(word_paste[i])
