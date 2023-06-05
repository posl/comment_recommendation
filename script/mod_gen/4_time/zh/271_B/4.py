def solve():
    n,q = list(map(int,input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(q):
        s,t = list(map(int,input().split()))
        print(arr[s-1][t-1])

if __name__ == '__main__':
    solve()