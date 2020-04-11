import timeit

###
def bubble_sort(numbers):
    # The swapped_flag is set to True in order for the loop
    # to iterate at least once.
    swapped_flag = True
    while swapped_flag:
        swapped_flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                # If the current number is larger than the next one,
                # perform a swap.
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                # Reset the flag to True in order to loop again.
                swapped_flag = True

###
def insertion_sort(numbers):
    # The first element is assumed to be sorted,
    # the iteration begins on the second element.
    for i in range(1, len(numbers)):
        element_to_insert = numbers[i]
        # Retain a reference to the previous element in the iteration.
        j = i - 1
        # Loop to move all of the larger elements forward.
        while j >= 0 and numbers[j] > element_to_insert:
            numbers[j + 1] = numbers[j]
            j -= 1
        # Inserts the current element in its correct position.
        numbers[j + 1] = element_to_insert

###
def selection_sort(numbers):
    # Loop iterates over the sorted items.
    for i in range(len(numbers)):
        # Assigns the first item of the unsorted array to be the smallest.
        # This is because we assume that the first item is the smallest.
        lowest_index = i
        # Loop iterates over the unsorted items.
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[lowest_index]:
                # If the old unsorted lowest number is larger than
                # the current number, the current number becomes the new lowest
                # number.
                lowest_index = j
        # Perform a swap on the current unsorted value and the lowest value.
        numbers[i], numbers[lowest_index] = numbers[lowest_index], \
        numbers[i]

###
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

    # Iterates over one shroter of the length of the given numbers array.
    # Iteration is backwards and stops at the first element of the array.
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)

###
def merge(left_list, right_list):
    sorted_list = []
    left_index = right_index = 0

    # Length variables for lists.
    left_list_length, right_list_length = len(left_list), len(right_list)

    # Iterate over the combined list lengths.
    for _ in range(left_list_length + right_list_length):
        # Checks to ensure that the lists haven't finished iterating.
        if left_index < left_list_length \
            and right_index < right_list_length:
            # Check which value of both lists is smaller.
            # If the left list item is smaller, add it to the sorted list.
            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            # Else, right list item is smaller, add it to the sorted list.
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1

        # If there are no more elements to iterate in the left list, add the
        # elements from the right list.
        elif left_index == left_list_length:
            sorted_list.append(right_list[right_index])
            right_index += 1
        # If there are no more elements to iterate in the right list, add the
        # elements from the left list.
        elif right_index == right_list_length:
            sorted_list.append(left_list[left_index])
            left_index += 1

    return sorted_list


def merge_sort(numbers):
    # Safety check to ensure the list is at least 2 elements in length.
    if len(numbers) <= 1:
        return numbers

    # Middle point is determined using floor devision of the array length.
    middle_point = len(numbers) // 2

    # Recursively sort each half of the array and store them in a list.
    left_list = merge_sort(numbers[:middle_point])
    right_list = merge_sort(numbers[middle_point:])

    # Merge the lists.
    return merge(left_list, right_list)

###
def partition(numbers, low_index, high_index):

    # Using floor division, the middle element is assigned to the pivot.
    pivot = numbers[(low_index + high_index) // 2]
    i = low_index - 1
    j = high_index + 1
    # Iterates through the list of numbers until it finds an element
    # that is to the right of the pivot point and is larger than an element to
    # the left of the pivot point.
    while True:
        i += 1
        while numbers[i] < pivot:
            i += 1

        j -= 1
        while numbers[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If such an element is found, swap it with the other element.
        numbers[i], numbers[j] = numbers[j], numbers[i]

# low_index - Pointer to the smaller elements based on the pivot.
# high_index - Pointer to the larger elements based on the pivot.
def quick_sort_helper(items, low_index, high_index):
    if low_index < high_index:
        # The index of the positions at which the lists are split.
        split_index = partition(items, low_index, high_index)
        quick_sort_helper(items, low_index, split_index)
        quick_sort_helper(items, split_index + 1, high_index)

def quick_sort(numbers):
    # A helper method is declared to enable correct recursive calling.
    quick_sort_helper(numbers, 0, len(numbers) - 1)


def run_algorithm(algorithm_name):
        
    word_paste = []
    runs = 30
    current = 0
    average = 0.0
    reversed_list_of_numbers = list(reversed(range(1, 5001)))

    print("List length: {}\n".format(len(reversed_list_of_numbers)))

    while current < runs:
        setup = ("from __main__ import {};".format(algorithm_name) +
                "reversed_list_of_numbers = {}".format(reversed_list_of_numbers))
        run_result = timeit.timeit(stmt="{}(reversed_list_of_numbers)"
                                .format(algorithm_name),
                                setup=setup, number=1)
        print("{} || Run {}: {}".format(algorithm_name, current + 1, run_result))
        word_paste.append(round(run_result, 6))
        average = average + run_result
        current = current + 1
    
    
    print("\nAverage: {}".format(average/runs))
    
    print("\nWord paste:")
    for i in range(len(word_paste)):
        print(word_paste[i])


run_algorithm(bubble_sort.__name__)
run_algorithm(insertion_sort.__name__)
run_algorithm(selection_sort.__name__)
run_algorithm(heap_sort.__name__)
run_algorithm(merge_sort.__name__)
run_algorithm(quick_sort.__name__)