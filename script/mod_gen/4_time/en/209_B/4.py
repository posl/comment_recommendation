def problems209_b():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if i % 2 == 0:
            total += A[i]
        else:
            total += A[i] - 1
    if total <= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problems209_b()