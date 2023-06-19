def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    bag = []
    for i in range(Q):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            bag = [x + query[i][1] for x in bag]
        elif query[i][0] == 3:
            print(min(bag))
            bag.pop(bag.index(min(bag)))
