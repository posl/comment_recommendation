def solution():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if sum([i % 2 for i in a]) != 0:
            break
        a = [i // 2 for i in a]
        ans += 1
    print(ans)

if __name__ == '__main__':
    solution()