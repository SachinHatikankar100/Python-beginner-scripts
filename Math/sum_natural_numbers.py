# Sum of natural numbers up to number

number = int(input('Enter the number: '))

if number < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate until zero
    while (number > 0):
        sum += number
        number -= 1
    # Outputting the sum of natural numbers
    print("The sum is", sum)
