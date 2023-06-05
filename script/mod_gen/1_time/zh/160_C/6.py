def main():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    A.append(A[0]+K)
    distance = []
    for i in range(N):
        distance.append(A[i+1]-A[i])
    print(K-max(distance))

if __name__ == '__main__':
    main()