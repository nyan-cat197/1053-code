# This code represents the single digits in a list as the larger integer it represents
# Since numbers are made up of ones, tens, hundreds etc. (powers of 10),
# we can represent any number through multiplication of powers of 10
# for example, the number 123 can be re-expressed as 1*10^2 + 2*10^1 + 3*10^0

def represent_as_int(lst): # creating a function for the program which will take a list as a parameter
    number = 0  # number we will be adding integers to, starting at 0
    power_of_ten = len(lst)-1 # since re-expressing numbers using powers of ten starts at 10^0, we need to -1 from the length of the list as the length of the list counts from 1 rather than 0


    for i in range(len(lst)):  # a loop which repeats the same function over the length of the list, starting at 0
        number = number + lst[i] * 10**(power_of_ten)  # Multiply each digit by the appropriate power of 10. ** represents exponent (^)
        power_of_ten = power_of_ten -1 #decrementing the power of 10 as we iterate through the list

    print(number) #prints the final number when the program is done running


represent_as_int([8, 3, 5, 1])
#output: 8351
represent_as_int([1,2,3,4,5])
#output: 12345
represent_as_int([2])
#output: 2
represent_as_int([])
#output: 0
