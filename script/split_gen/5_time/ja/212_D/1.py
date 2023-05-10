def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    
    bag = []
    min_value = 0
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
        elif query[0] == 2:
            for i in range(len(bag)):
                bag[i] += query[1]
        elif query[0] == 3:
            min_value = min(bag)
            print(min_value)
            bag.remove(min_value)
