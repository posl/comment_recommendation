def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    if A < 3 or A > 9 or B < 3 or B > 9:
        print("输入错误")
    else:
        print(32 ** (A - B))

if __name__ == '__main__':
    main()