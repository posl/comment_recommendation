def main():
    q = int(input())
    s = []
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            count = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == x:
                    s.pop(i)
                    count += 1
                    if count == c:
                        break
        else:
            print(max(s) - min(s))

if __name__ == '__main__':
    main()