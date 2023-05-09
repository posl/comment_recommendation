def main():
    Q = int(input())
    bag = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[1])
        elif query[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()