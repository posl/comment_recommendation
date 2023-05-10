def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A = list(map(lambda x:x-1,A))
    A[X-1] = -1
    counter = 1
    for i in range(N):
        if A[i] == -1:
            continue
        else:
            counter += 1
            A[A[i]] = -1
    print(counter)

if __name__ == '__main__':
    main()