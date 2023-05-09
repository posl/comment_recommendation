def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = zip(*sorted(zip(A, B)))
    time = 0
    for i in range(N):
        time += A[i]
        if time > B[i]:
            print("No")
            return
    print("Yes")
main()
