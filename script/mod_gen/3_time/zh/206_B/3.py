def solve():
    #n = int(input())
    n = 12
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if sum >= n:
            print(i)
            break

if __name__ == '__main__':
    solve()