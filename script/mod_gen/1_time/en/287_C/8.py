def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    else:
        print("Yes")
        return

if __name__ == '__main__':
    main()