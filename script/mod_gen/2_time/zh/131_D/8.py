def solution():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[1])
    t = 0
    for a, b in ab:
        t += a
        if t > b:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solution()