def main():
    n = int(input())
    a = input().split()
    a = set(a)
    if len(a) == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()