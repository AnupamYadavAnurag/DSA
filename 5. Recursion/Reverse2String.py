def re(s):
    if len(s)<=1:
        return s
    return re(s[1:])+s[0]
print(re("Anupam"))