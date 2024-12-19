#Problem 3
Thickness = 0.00008

for times_folded in range(44):
    folded_thickness_1 = Thickness * 2**times_folded
    if times_folded == 44:
        break;

print("Thickness: {} meters".format(folded_thickness_1))