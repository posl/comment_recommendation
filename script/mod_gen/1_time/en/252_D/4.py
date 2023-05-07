def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i] == A[j]:
                continue
            for k in range(j+1,N):
                if A[j] == A[k] or A[i] == A[k]:
                    continue
                if A[i] + A[j] > A[k]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()