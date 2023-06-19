def main():
    A_1, A_2, A_3 = map(int, input().split())
    if A_1 + A_2 + A_3 >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()