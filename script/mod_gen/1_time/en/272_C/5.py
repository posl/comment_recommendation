def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    B = [A[0]]
    for i in range(1,N):
        if A[i] == A[i-1]:
            B.append(A[i])
        else:
            if len(B) >= 2:
                if B[-1] % 2 == 0:
                    print(B[-1])
                    return
                else:
                    B.pop()
            B.append(A[i])
    print(-1)

if __name__ == '__main__':
    main()