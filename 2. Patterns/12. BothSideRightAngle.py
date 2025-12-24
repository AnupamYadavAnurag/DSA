for i in range(1, 4 + 1):
    # Left numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Middle spaces
    print("  " * (2 * (4 - i)), end="")
    
    # Right numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()
