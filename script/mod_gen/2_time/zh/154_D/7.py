def main():
    n = int(input())
    a = input().split()
    if len(set(a)) == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()