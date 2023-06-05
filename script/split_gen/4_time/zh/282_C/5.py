def solve():
    n = int(input())
    s = input()
    for i in range(1, n+1):
        if i % 2 == 0:
            print(s[i-1], end="")
        else:
            if s[i-1] == ",":
                print(",", end="")
            else:
                print(".", end="")
    print()
solve()
