n = 4
for i in range(1, n + 1):
    # Left numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Middle spaces
    print("  " * (2 * (n - i)), end="")
    
    # Right numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()
