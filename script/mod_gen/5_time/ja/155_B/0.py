def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

if __name__ == '__main__':
    main()