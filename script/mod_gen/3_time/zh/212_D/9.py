def main():
    q = int(input())
    query = [list(map(int,input().split())) for _ in range(q)]
    bag = []
    min = 0
    for i in range(q):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            bag = [x + query[i][1] for x in bag]
        else:
            min = min(bag)
            bag.remove(min)
            print(min)

if __name__ == '__main__':
    main()