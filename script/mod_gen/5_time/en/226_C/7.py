def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        T.append(list(map(int, input().split())))
        A.append(list(map(int, input().split())))
    print(N)
    print(T)
    print(A)

if __name__ == '__main__':
    main()