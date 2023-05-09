def solve():
    n = int(input())
    h = list(map(int,input().split()))
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]
            index = i + 1
    print(index)

if __name__ == '__main__':
    solve()