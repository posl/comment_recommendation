def main():
    a_1, a_2, a_3 = map(int, input().split())
    if a_3-a_2==a_2-a_1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()