def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_ = max(A)
    max_i = A.index(max_)
    A.pop(max_i)
    max_2 = max(A)
    for i in range(N):
        if i == max_i:
            print(max_2)
        else:
            print(max_)

if __name__ == '__main__':
    main()