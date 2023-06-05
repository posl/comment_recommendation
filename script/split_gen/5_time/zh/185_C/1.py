def cut(L):
    if L == 12:
        return 1
    else:
        return L-1 + cut(L-1)
print(cut(17))
