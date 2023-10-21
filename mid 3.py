try:
    def generate_fibonacci_sequence(length):
        sequence = []
        sequence.append(1)
        sequence.append(1)

        for i in range(2, length):
            sequence.append(sequence[i - 1] + sequence[i - 2])

        return sequence


    length = int(input("Please enter the length of Fibonacci sequence "))
    sequence = generate_fibonacci_sequence(length)
    print("The Fibonacci sequence for " + str(length) + " is " + str(sequence))
except ValueError:
    print("Error")