def main():
    Q = int(input())
    bag = []
    add = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            bag.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            print(min(bag) + add)
            bag.remove(min(bag))

if __name__ == '__main__':
    main()