def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    i = 0
    count = 0
    while True:
        i = A[i]-1
        count += 1
        if i == 0:
            break
    K = K % count
    i = 0
    for j in range(K):
        i = A[i]-1
    print(i+1)

if __name__ == '__main__':
    main()