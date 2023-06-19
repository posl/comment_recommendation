def solve():
    n = int(input())
    total = 4*n
    a = list(map(int, input().split()))
    sum = 0
    for i in a:
        sum += i
    print(sum - total*(total+1)//2)

if __name__ == '__main__':
    solve()