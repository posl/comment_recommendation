def main():
    N = int(input())
    for x in range(1,10):
        for y in range(1,10):
            if N == x * y:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()