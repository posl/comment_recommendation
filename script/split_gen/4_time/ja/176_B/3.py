def solve():
    n = input()
    s = 0
    for c in n:
        s += int(c)
    if s % 9 == 0:
        print("Yes")
    else:
        print("No")
