def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        if i % 2 == 0:
            B.append(i + 1)
        else:
            C.append(i + 1)
    print("Yes")
    print(len(B), *B)
    print(len(C), *C)

if __name__ == '__main__':
    main()