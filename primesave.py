import primelookupgen

n = int(input("What's the highest number (exclusive) you want to check?\n"))

A = primelookupgen.gen_lookup_table(n)

with open("primes.txt", mode="w") as f:
    for i in range(n):
        if A[i]:
            f.write(str(i) + "\n")

print("The results have been saved in 'primes.txt'")
input("Press enter to close...\n")
