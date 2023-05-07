def main():
    a, b = map(int, input().split())
    for i in range(a + 1):
        for j in range(a + 1):
            if i + j == b:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()