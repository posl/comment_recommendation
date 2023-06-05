def solve():
    n, k, q = map(int, input().split())
    score = [k for _ in range(n)]
    for _ in range(q):
        a = int(input())
        score[a - 1] += 1
    for i in range(n):
        if score[i] <= q:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    solve()