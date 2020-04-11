import timeit
import random

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


random_list_of_numbers = random.sample(range(1, 5001), 5000)
print("List length: {}\n".format(len(random_list_of_numbers)))
word_paste = []
runs = 30
current = 0
average = 0.0

while current < runs:
    setup = ("from __main__ import merge_sort;"
             "random_list_of_numbers = {}".format(random_list_of_numbers))
    run_result = timeit.timeit(stmt="merge_sort(random_list_of_numbers)",
                               setup=setup, number=1)
    word_paste.append(round(run_result, 6))
    print("Run {}: {}".format(current + 1, run_result))
    average = average + run_result
    current = current + 1

print("\nAverage: {}".format(average/runs))

print("\nWord paste:")
for i in range(len(word_paste)):
    print(word_paste[i])
