def solve():
    N = int(input())
    if N >= -2**31 and N <= 2**31-1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()