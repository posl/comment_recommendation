def solve():
    # Implement solution here
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(min(max(A), max(B)))

if __name__ == '__main__':
    solve()