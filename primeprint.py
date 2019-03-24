import primegen
import time

n = int(input("What's the highest number (exclusive) you want to check?\n"))

start_time = time.time()

A = primegen.gen_lookup_table(n)
for i in range(n):
    if A[i]:
        print(i)

print("Run time: ", end="")
print(time.time() - start_time, end="")
print("s")

input("Press enter to close...\n")
