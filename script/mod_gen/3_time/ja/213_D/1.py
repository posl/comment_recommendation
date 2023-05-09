def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i],B[i] = map(int,input().split())
    
    route = [1]
    now = 1
    i = 0
    while True:
        if A[i] == now:
            route.append(B[i])
            now = B[i]
        elif B[i] == now:
            route.append(A[i])
            now = A[i]
        i += 1
        if i == N-1:
            i = 0
        if now == 1:
            break
    print(" ".join(map(str,route)))

if __name__ == '__main__':
    main()