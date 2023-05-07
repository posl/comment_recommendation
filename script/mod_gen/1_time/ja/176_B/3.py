def solve():
    import sys
    readline = sys.stdin.buffer.readline
    n = readline().rstrip().decode('utf-8')
    if int(n)%9==0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()