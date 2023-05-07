def main():
    # 自分の解答
    # A, B, C = map(int, input().split())
    # if A * C <= B:
    #     print(C)
    # else:
    #     print(B // A)
    # 他の人の解答
    A, B, C = map(int, input().split())
    print(min(B//A, C))

if __name__ == '__main__':
    main()