def main():
    n = int(input())
    bag = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for i in range(len(bag)):
                bag[i] += int(query[1])
        elif query[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()