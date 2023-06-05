def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    for i in range(N):
        C.append([B[i], A[i]])
    C.sort()
    t = 0
    for i in range(N):
        t += C[i][1]
        if t > C[i][0]:
            print("No")
            return
    print("Yes")
    return
