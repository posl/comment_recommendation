def main():
    # Read from STDIN
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    # Solve
    bag = []
    bag_min = 10**9 + 1
    bag_min_index = None
    for i in range(Q):
        if queries[i][0] == 1:
            bag.append(queries[i][1])
            if queries[i][1] < bag_min:
                bag_min = queries[i][1]
                bag_min_index = len(bag) - 1
        elif queries[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += queries[i][1]
                if bag[j] < bag_min:
                    bag_min = bag[j]
                    bag_min_index = j
        else:
            print(bag[bag_min_index])
            del bag[bag_min_index]
            bag_min = 10**9 + 1
            for j in range(len(bag)):
                if bag[j] < bag_min:
                    bag_min = bag[j]
                    bag_min_index = j
