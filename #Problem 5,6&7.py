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
