def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.append(A[0]+360)
    max = 0
    for i in range(N):
        if A[i+1]-A[i] > max:
            max = A[i+1]-A[i]
    print(360-max)

if __name__ == '__main__':
    main()