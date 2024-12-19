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