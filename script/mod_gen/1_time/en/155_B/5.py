def main():
    N = int(input())
    A = list(map(int, input().split()))
    for x in A:
        if x % 2 == 0:
            if x % 3 != 0 and x % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return
main()

if __name__ == '__main__':
    main()