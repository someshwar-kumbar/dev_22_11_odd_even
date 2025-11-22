import sys
if len(sys.argv) < 2:
    print("Usage: python3 counter.py <num1> <num2> ...")
    sys.exit(1)
num = list(map(int, sys.argv[1:]))
even_count = 0
odd_count = 0
for n in num:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Numbers:", num)
print("Even count:", even_count)
print("Odd count:", odd_count)
