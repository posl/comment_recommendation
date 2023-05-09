def main():
    Q = int(input())
    bag = []
    add = 0
    for i in range(Q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            bag.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            min = 10**9
            for j in range(len(bag)):
                if bag[j] < min:
                    min = bag[j]
                    index = j
            print(min + add)
            bag.pop(index)
