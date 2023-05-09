def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = min(A) + min(B)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                time = max(A[i], B[j])
                if time < min_time:
                    min_time = time
    print(min_time)

if __name__ == '__main__':
    main()