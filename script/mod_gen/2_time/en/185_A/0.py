def main():
    a1, a2, a3, a4 = map(int, input().split())
    if a1 + a2 + a3 + a4 >= 10:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()