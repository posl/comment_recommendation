def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    if len(s) == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()