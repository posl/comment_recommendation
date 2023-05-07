def main():
    A, B = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if A == 2 and i + j == B:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()