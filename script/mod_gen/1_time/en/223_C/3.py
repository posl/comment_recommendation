def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i]/B[i]
        right += A[N-i-1]/B[N-i-1]
    if left == right:
        print(left)
    else:
        left = 0
        right = 0
        for i in range(N):
            left += A[i]/B[i]
            right += A[N-i-1]/B[N-i-1]
            if left == right:
                print(left)
                break
            elif left > right:
                for j in range(i+1,N):
                    left += A[j]/B[j]
                    right += A[N-j-1]/B[N-j-1]
                    if left == right:
                        print(left)
                        break
                    elif left > right:
                        continue
                    else:
                        print(left)
                        break
            else:
                for j in range(i+1,N):
                    left += A[j]/B[j]
                    right += A[N-j-1]/B[N-j-1]
                    if left == right:
                        print(left)
                        break
                    elif left > right:
                        print(right)
                        break
                    else:
                        continue
        else:
            print(left)
main()

if __name__ == '__main__':
    main()