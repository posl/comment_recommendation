def main():
    Q = int(input())
    query = [input().split() for i in range(Q)]
    bag = []
    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]))
        elif query[i][0] == '2':
            bag = [x + int(query[i][1]) for x in bag]
        elif query[i][0] == '3':
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()