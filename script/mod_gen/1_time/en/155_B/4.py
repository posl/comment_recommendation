def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in A:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return
main()

if __name__ == '__main__':
    main()