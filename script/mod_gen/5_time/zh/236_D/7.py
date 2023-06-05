def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    print(A)

if __name__ == '__main__':
    main()