import timeit
import random

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


random_list_of_numbers = random.sample(range(1, 5001), 5000)
print("List length: {}\n".format(len(random_list_of_numbers)))
word_paste = []
runs = 30
current = 0
average = 0.0

while current < runs:
    setup = ("from __main__ import quick_sort;"
             "random_list_of_numbers = {}".format(random_list_of_numbers))
    run_result = timeit.timeit(stmt="quick_sort(random_list_of_numbers)",
                               setup=setup, number=1)
    word_paste.append(round(run_result, 6))
    print("Run {}: {}".format(current + 1, run_result))
    average = average + run_result
    current = current + 1

print("\nAverage: {}".format(average/runs))

print("\nWord paste:")
for i in range(len(word_paste)):
    print(word_paste[i])
