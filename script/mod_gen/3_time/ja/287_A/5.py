def main():
    n = int(input())
    a = [input() for _ in range(n)]
    if a.count("For") > n//2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()