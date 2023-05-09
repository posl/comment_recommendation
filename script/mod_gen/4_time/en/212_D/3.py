def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    bag = []
    for q in queries:
        if q[0] == 1:
            bag.append(q[1])
        elif q[0] == 2:
            for i in range(len(bag)):
                bag[i] += q[1]
        elif q[0] == 3:
            print(min(bag))
            bag.pop(bag.index(min(bag)))

if __name__ == '__main__':
    main()