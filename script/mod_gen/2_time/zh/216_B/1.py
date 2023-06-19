def main():
    n = int(input())
    a = [input().split() for i in range(n)]
    print("Yes" if len(set(tuple(i) for i in a)) < n else "No")

if __name__ == '__main__':
    main()