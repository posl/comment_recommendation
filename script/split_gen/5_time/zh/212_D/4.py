def main():
    #输入
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int,input().split())))
    #处理
    bag = []
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
        elif query[0] == 2:
            bag = [x+query[1] for x in bag]
        elif query[0] == 3:
            print(min(bag))
            bag.remove(min(bag))
