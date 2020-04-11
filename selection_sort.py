import timeit
import random

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


random_list_of_numbers = random.sample(range(1, 5001), 5000)
print("List length: {}\n".format(len(random_list_of_numbers)))
word_paste = []
runs = 30
current = 0
average = 0.0

while current < runs:
    setup = ("from __main__ import selection_sort;"
             "random_list_of_numbers = {}".format(random_list_of_numbers))
    run_result = timeit.timeit(stmt="selection_sort(random_list_of_numbers)",
                               setup=setup, number=1)
    word_paste.append(round(run_result, 6))
    print("Run {}: {}".format(current + 1, run_result))
    average = average + run_result
    current = current + 1

print("\nAverage: {}".format(average/runs))

print("\nWord paste:")
for i in range(len(word_paste)):
    print(word_paste[i])
