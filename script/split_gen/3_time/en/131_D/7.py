def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    X = sorted(zip(B, A), reverse = True)
    t = 0
    for b, a in X:
        t += a
        if t > b:
            print("No")
            return
    print("Yes")
