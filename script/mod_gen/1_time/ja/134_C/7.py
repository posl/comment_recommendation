def main():
    #入力
    N = int(input())
    A = [int(input()) for i in range(N)]
    #解答
    A.sort()
    for i in range(N):
        if i == 0:
            print(A[-2])
        elif i == N-1:
            print(A[-2])
        else:
            print(A[-1])

if __name__ == '__main__':
    main()