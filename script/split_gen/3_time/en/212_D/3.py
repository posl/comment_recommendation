def main():
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(input().split())
    bag = []
    add = 0
    for query in queries:
        if query[0] == "1":
            bag.append(int(query[1]) - add)
        elif query[0] == "2":
            add += int(query[1])
        else:
            print(min(bag) + add)
            bag.remove(min(bag))
