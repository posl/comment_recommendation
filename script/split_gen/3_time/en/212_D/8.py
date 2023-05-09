def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(input().split())
    #print(query)
    bag = []
    add = 0
    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]) - add)
        elif query[i][0] == '2':
            add += int(query[i][1])
        else:
            bag.sort()
            print(bag[0] + add)
            bag.pop(0)
