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
            for j in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        else:
            print(max(s)-min(s))
main()

if __name__ == '__main__':
    main()