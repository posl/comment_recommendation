def d():
    n = int(input())
    queries = [list(map(int, input().split())) for _ in range(n)]
    bag = []
    min_num = 10**9
    for query in queries:
        if query[0] == 1:
            bag.append(query[1])
            if min_num > query[1]:
                min_num = query[1]
        elif query[0] == 2:
            bag = [i + query[1] for i in bag]
            min_num += query[1]
        else:
            print(min_num)
            bag.remove(min_num)
            if len(bag) != 0:
                min_num = min(bag)
            else:
                min_num = 10**9
