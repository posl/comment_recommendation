def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    bag = []
    min = 0
    for i in range(q):
        if query[i][0] == 1:
            bag.append(query[i][1])
        elif query[i][0] == 2:
            bag = [x + query[i][1] for x in bag]
        elif query[i][0] == 3:
            min = bag.index(min(bag))
            print(bag[min])
            del bag[min]
