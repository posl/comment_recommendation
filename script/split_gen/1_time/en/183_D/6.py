def main():
    N, W = map(int, input().split())
    A = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        A.append((s, p))
        A.append((t, -p))
    A.sort()
    now = 0
    for i in range(len(A)):
        now += A[i][1]
        if now > W:
            print("No")
            return
    print("Yes")
