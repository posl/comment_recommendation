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
            for j in range(min(c, s.count(x))):
                s.remove(x)
        else:
            print(max(s) - min(s))

if __name__ == '__main__':
    main()