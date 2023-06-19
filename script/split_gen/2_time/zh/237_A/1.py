def solve():
    n = int(input())
    if n >= -2**31 and n <= 2**31-1:
        print("是")
    else:
        print("否")
solve()
