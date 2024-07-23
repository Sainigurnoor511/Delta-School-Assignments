'''
You are given a list of integers representing the daily temperatures for a week. Write a Python script using NumPy to perform the following tasks:
Convert the list of temperatures into a NumPy array.
Reshape the array to a 2x3 matrix.
Calculate the average temperature for each row (i.e., for the first half of the week and the second half of the week).
Find the highest temperature of the week.
Create a boolean mask to identify temperatures greater than
than the average temperature of the week.
'''

import numpy as np

list_temp = [31, 34, 45, 32, 30, 32] #Temp in Celsius

arr_temp = np.array(list_temp)

reshaped_arr_temp = arr_temp.reshape(2, 3)
print("Array of Temperatures:\n", reshaped_arr_temp)

temp_matrix = reshaped_arr_temp

avg_temp_row1 = np.mean(temp_matrix[0])
avg_temp_row2 = np.mean(temp_matrix[1])
print("Average Temperatures Row 1:", avg_temp_row1)
print("Average Temperatures Row 2:", avg_temp_row2)

max_temp = np.max(arr_temp)
avg_temp_week = np.mean(arr_temp)

print("Max Temperature of the week:", max_temp)

bool_mask = arr_temp > avg_temp_week
print("Temperatures greater than the average temperature of the week:")
print(list_temp)
print(bool_mask)
print(arr_temp[bool_mask])