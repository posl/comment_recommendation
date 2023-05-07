def main():
    a, b = map(int, input().split())
    for i in range(a):
        for j in range(a):
            if (i + 1) + (j + 1) == b:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()