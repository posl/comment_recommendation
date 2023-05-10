def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    balls = set()
    for i in range(N):
        if i == 0:
            balls.add(A[i])
        else:
            if A[i] in balls:
                balls.remove(A[i])
            else:
                balls.add(A[i])
    print(len(balls))

if __name__ == '__main__':
    main()