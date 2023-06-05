def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] != a[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    solve()