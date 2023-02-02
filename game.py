insert = 0
for numbers in range(1, 101):
    insert = numbers
    if insert % 3 == 0 and insert % 5 == 0:
        print("FizzBuzz")
    elif insert % 3 == 0:
        print("Fizz")
    elif insert % 5 == 0:
        print("Buzz")
    else:
        print(numbers)
