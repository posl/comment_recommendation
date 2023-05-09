def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)
    bag = []
    add = 0
    for i in range(Q):
        if query[i][0] == 1:
            bag.append(query[i][1] - add)
        elif query[i][0] == 2:
            add += query[i][1]
        else:
            bag.sort()
            print(bag[0] + add)
            bag.pop(0)
