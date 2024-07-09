# Create a dictionary with the names and ages of your friends.

age = {"Gurnoor": 20, "Vivek": 21, "Dinesh": 22, "Harsh": 23}


# Write a program to update the score of a student and print the updated dictionary.

marks = {"Gurnoor": 90, "Vivek": 80, "Dinesh": 70, "Harsh": 60}
print(marks)

name = input("Enter the name you want to update marks for: ")
new_mark = int(input("Enter the new mark: "))
marks[name] = new_mark
print(marks)