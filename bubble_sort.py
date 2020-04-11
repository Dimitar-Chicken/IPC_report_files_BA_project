import timeit
import random

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

random_list_of_numbers = random.sample(range(1, 5001), 5000)
print("List length: {}\n".format(len(random_list_of_numbers)))
word_paste = []
runs = 30
current = 0
average = 0.0

while current < runs:
    setup = ("from __main__ import bubble_sort;"
             "random_list_of_numbers = {}".format(random_list_of_numbers))
    run_result = timeit.timeit(stmt="bubble_sort(random_list_of_numbers)",
                               setup=setup, number=1)
    word_paste.append(round(run_result, 6))
    print("Run {}: {}".format(current + 1, run_result))
    average = average + run_result
    current = current + 1

print("\nAverage: {}".format(average/runs))

print("\nWord paste:")
for i in range(len(word_paste)):
    print(word_paste[i])
