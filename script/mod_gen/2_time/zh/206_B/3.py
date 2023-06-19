def problem206_b():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i
        if ans >= n:
            print(i)
            break

if __name__ == '__main__':
    problem206_b()