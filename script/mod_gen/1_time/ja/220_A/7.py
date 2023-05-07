def main():
    # A, B, C = map(int, input().split())
    # print(A, B, C)
    # for i in range(A, B + 1):
    #     if i % C == 0:
    #         print(i)
    #         break
    # else:
    #     print(-1)
    A, B, C = map(int, input().split())
    print(next(filter(lambda x: x % C == 0, range(A, B + 1)), -1))

if __name__ == '__main__':
    main()