def solve():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        sum += i
    print(sum)

if __name__ == '__main__':
    solve()