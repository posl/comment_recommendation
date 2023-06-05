def cut(L):
    if L < 12:
        return 0
    if L == 12:
        return 1
    if L == 13:
        return 12
    if L == 14:
        return 36
    if L == 15:
        return 92
    if L == 16:
        return 232
    if L == 17:
        return 596
    return cut(L-1) + cut(L-2) + cut(L-3) + cut(L-4) + cut(L-5) + cut(L-6)
L = int(input())
print(cut(L))
