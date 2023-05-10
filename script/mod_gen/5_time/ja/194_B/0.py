def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        line = input().split(" ")
        A.append(int(line[0]))
        B.append(int(line[1]))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = max(ans, A[i] + B[j])
            else:
                ans = max(ans, max(A[i], B[j]))
    print(ans)

if __name__ == '__main__':
    main()