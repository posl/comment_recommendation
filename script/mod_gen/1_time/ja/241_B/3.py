def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if B[i] < A[0]:
            print("No")
            return
        elif B[i] > A[N-1]:
            print("No")
            return
        else:
            a = 0
            b = N-1
            while True:
                c = (a+b)//2
                if A[c] == B[i]:
                    print("No")
                    return
                elif A[c] > B[i]:
                    if A[c-1] < B[i]:
                        print("No")
                        return
                    else:
                        b = c
                elif A[c] < B[i]:
                    if A[c+1] > B[i]:
                        print("Yes")
                        break
                    else:
                        a = c
    return

if __name__ == '__main__':
    main()