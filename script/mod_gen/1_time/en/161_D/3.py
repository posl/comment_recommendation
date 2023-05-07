def solve():
    K = int(input())
    q = [i for i in range(1, 10)]
    for _ in range(K):
        x = q.pop(0)
        for i in range(-1, 2):
            y = x % 10 + i
            if y >= 0 and y <= 9:
                q.append(x * 10 + y)
    print(x)
solve()

if __name__ == '__main__':
    solve()