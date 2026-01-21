def PrintNumber(Lrange, Urange):
    # Base CAse
    if Lrange > Urange:
        return
    PrintNumber(Lrange + 1, Urange)
    print(Lrange,Urange)

PrintNumber(1,10)
