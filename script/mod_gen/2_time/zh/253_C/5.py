def main():
    q = int(input())
    a = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(c):
                if x in a:
                    a.remove(x)
                else:
                    break
        else:
            print(max(a)-min(a))

if __name__ == '__main__':
    main()