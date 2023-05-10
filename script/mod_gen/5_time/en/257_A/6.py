def solve():
    N,X = map(int,input().split())
    print(chr(ord('A')+X//N-1))

if __name__ == '__main__':
    solve()