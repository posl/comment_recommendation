def main():
    q = int(input())
    ans = 0
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            ans += int(query[1]) * int(query[2])
        else:
            print(ans)
            ans = 0

if __name__ == '__main__':
    main()