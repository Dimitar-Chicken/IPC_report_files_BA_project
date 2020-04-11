import timeit
import random

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


random_list_of_numbers = random.sample(range(1, 5001), 5000)
print("List length: {}\n".format(len(random_list_of_numbers)))
word_paste = []
runs = 30
current = 0
average = 0.0

while current < runs:
    setup = ("from __main__ import insertion_sort;"
             "random_list_of_numbers = {}".format(random_list_of_numbers))
    run_result = timeit.timeit(stmt="insertion_sort(random_list_of_numbers)",
                               setup=setup, number=1)
    word_paste.append(round(run_result, 6))
    print("Run {}: {}".format(current + 1, run_result))
    average = average + run_result
    current = current + 1

print("\nAverage: {}".format(average/runs))

print("\nWord paste:")
for i in range(len(word_paste)):
    print(word_paste[i])
