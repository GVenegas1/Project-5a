# project-5a

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 10/29/2025
# Description: This program takes a list of numbers and returns the medium value.

def find_median(numbers):
    """Find the median of a list of numbers.If there are even
        number of items, then it returns the average of the two middle numbers. """

    #sort the list
    numbers.sort()

    #find how many numbers are in the list
    n = len(numbers)

    #find the middle position
    middle = n // 2
    #if oddnumber of items, return the middle one
    if n % 2 == 1:
        return numbers[middle]
    else:
        #if even, return average of two middle numbers
        return (numbers[middle - 1] + numbers[middle]) / 2

#example used
#some_nums=[13,7,-3,82,4]
#result= find_median(some_nums)
#print("The medium is:", result)