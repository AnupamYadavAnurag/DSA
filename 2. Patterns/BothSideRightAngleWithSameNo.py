for i in range(1, 5):
    # Left numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Middle spaces
    print("  " * (2 * (4 - i)), end="")
    
    # Right numbers
    for k in range(i, 0, - 1):
        print(k, end=" ")
    
    print()
