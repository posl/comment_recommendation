def solve():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    if s.count("For") > n//2:
        print("Yes")
    else:
        print("No")