def main():
    Q = int(input())
    ans = []
    total = 0
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            total += int(query[1]) * int(query[2])
        else:
            ans.append(total)
            total = 0
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()