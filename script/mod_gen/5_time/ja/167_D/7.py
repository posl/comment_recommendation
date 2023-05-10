def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    T = [1]
    T.append(A[0])
    i = 0
    while(1):
        i = T[i]
        T.append(A[i-1])
        if(T[i] == 1):
            break
    if(K < len(T)):
        print(T[K])
    else:
        K -= i
        K %= (len(T) - i)
        print(T[i+K])

if __name__ == '__main__':
    main()