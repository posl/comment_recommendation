def main():
    q = int(input())
    L = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            L.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for i in range(c):
                if x in L:
                    L.remove(x)
                else:
                    break
        elif query[0] == '3':
            print(max(L) - min(L))

if __name__ == '__main__':
    main()