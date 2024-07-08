# Define a function that takes a list of
# numbers and returns the sum of these numbers
#
# Author: Gurnoor Singh Saini

def sum_of_list(list_num):
    sum = 0
    for num in list_num:
        sum += num
    return sum

list_num=[]
n = int(input("Enter number of elements :"))

for i in range (n):
    print(f"Enter the {i+1} element :")
    x = int(input())
    list_num.append(x)

print("List of elements :" , list_num)
print("Sum of elements :" , sum_of_list(list_num))