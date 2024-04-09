def find_second_min(numbers):

    unique_numbers = sorted(set(numbers))

    assert len(unique_numbers) == 3,2

     
    return unique_numbers[1]

numbers = [10, 5, 8, 3, 9, 2, 7]

result = find_second_min(numbers)

print("друге мінімальне чісло:", result) 

assert find_second_min([5, 8, 3, 2, 8]) == 3 