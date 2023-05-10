def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        s = input().split()
        if s[0] == '1':
            a[int(s[1])-1] = int(s[2])
        else:
            print(a[int(s[1])-1])

if __name__ == '__main__':
    main()