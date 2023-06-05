def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = sorted(zip(A, B), key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += C[i][0]
        if t > C[i][1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()