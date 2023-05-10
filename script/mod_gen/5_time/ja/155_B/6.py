def main():
    num = int(input())
    A = list(map(int, input().split()))
    flag = True
    for i in A:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                flag = False
    if flag:
        print("APPROVED")
    else:
        print("DENIED")

if __name__ == '__main__':
    main()