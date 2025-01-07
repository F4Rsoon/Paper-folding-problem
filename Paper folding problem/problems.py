#Problem 1
# Code to calculate the thickness when the paper is folded once

THICKNESS = 0.00008

folded_thickness = THICKNESS * 2**43

print("Thickness: {} meters".format(folded_thickness))

#Problem 2
# Convert meters to kilometers and display with two decimal places
print("Thickness: {: .2f} kilometers".format(folded_thickness / 1000))


#Problem 3
Thickness = 0.00008

for times_folded in range(44):
    folded_thickness_1 = Thickness * 2**times_folded
    if times_folded == 44:
        break;

print("Thickness: {} meters".format(folded_thickness_1))


#Problem 4

import time

start = time.time()
THICKNESS = 0.00008
elapsed_time_exp = time.time() - start
folded_thickness = THICKNESS * 2**43

print("Thickness: {} meters".format(folded_thickness))
print("Time (Exponentiation): {:.10f} seconds".format(elapsed_time_exp))

start = time.time()
Thickness = 0.00008

for times_folded in range(44):
    folded_thickness_1 = Thickness * 2**times_folded
    if times_folded == 44:
        break;

elapsed_time_loop = time.time() - start
print("Thickness: {} meters".format(folded_thickness_1))
print("Time (For loop): {:.10f} seconds".format(elapsed_time_loop))


#Problem 5
import matplotlib.pyplot as plt

THICKNESS = 0.00008
thickness_list = []

current_thickness = THICKNESS
for fold in range(44):
    thickness_list.append(current_thickness)
    current_thickness *= 2

print("Number of values in the list:", len(thickness_list))

#Problem 6
plt.figure(figsize=(10, 6))
plt.plot(range(44), thickness_list, marker='o', label="Paper Thickness")
plt.title("Exponential Growth of Paper Thickness", fontsize=16)
plt.xlabel("Number of Folds", fontsize=14)
plt.ylabel("Thickness (meters)", fontsize=14)
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12)
plt.show()


#Problem 7
plt.figure(figsize=(10, 6))
plt.plot(range(44), thickness_list, color='orange', linewidth=2.5, label="Thickness (Orange Line)")
plt.title("Exponential Growth of Paper Thickness", fontsize=16)
plt.xlabel("Number of Folds", fontsize=16)
plt.ylabel("Thickness (meters)", fontsize=16)
plt.tick_params(labelsize=14)
plt.yscale("log")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend(fontsize=14)
plt.show()
