def main():
    str1, str2 = input().split()
    str3 = input()
    A, B = map(int, input().split())
    if str1 == str3:
        A -= 1
    else:
        B -= 1
    print(A, B)

if __name__ == '__main__':
    main()