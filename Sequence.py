numbersGenerated = input("How many numbers of the Fibonacci would you like to generate?\n") # decides how many numbers of the fibonacci sequence will be generated
sequence = [0, 1] # the first twi terms of the fibonacci sequence
for i in range(int(numbersGenerated) -2): # starts a loop to generate how many numbers have been inputted
    nextTerm = sequence[i] + sequence[i+1] # generates the next term by adding the previous two terms
    sequence.append(nextTerm)  # adds the next term to the list
print(sequence)  # prints the amount of number in the fibonacci inputted
print(len(sequence)) # verifies that the correct amount of number have been outputted