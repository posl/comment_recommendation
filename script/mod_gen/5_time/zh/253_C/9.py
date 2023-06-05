def main():
    q = int(input())
    s = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            count = 0
            for j in range(len(s)):
                if s[j] == x:
                    s.pop(j)
                    count += 1
                    if count == c:
                        break
        elif query[0] == '3':
            print(max(s) - min(s))

if __name__ == '__main__':
    main()