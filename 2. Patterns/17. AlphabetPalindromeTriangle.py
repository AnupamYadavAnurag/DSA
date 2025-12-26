for i in range(1, 5):
    # Spaces
    print(" " * (5 - i), end="")
    
    # Increasing alphabets
    for j in range(i):
        print(chr(65 + j), end="")
    
    # Decreasing alphabets
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    
    print()
