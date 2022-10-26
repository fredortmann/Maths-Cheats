def productFib(prod):
    fibonacci_numbers = [0, 1]
    for i in range(2, 150):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

    for num in range(150):

        if fibonacci_numbers[num] * fibonacci_numbers[num + 1] == prod:
            return [fibonacci_numbers[num], fibonacci_numbers[num + 1], True]

        elif fibonacci_numbers[num] * fibonacci_numbers[num + 1] >= prod:
            return [fibonacci_numbers[num], fibonacci_numbers[num + 1], False]

