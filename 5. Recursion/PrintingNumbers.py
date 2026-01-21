def PrintNumbers(Lrange , Urange):
    # Base Case 
    if Lrange > Urange:
        return
    print(Lrange)
    PrintNumbers(Lrange + 1 , Urange)

PrintNumbers(1, 10)