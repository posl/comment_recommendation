def main():
    q = int(input())
    op = []
    for i in range(q):
        op.append(list(map(int, input().split())))
    bag = []
    for i in range(q):
        if op[i][0] == 1:
            bag.append(op[i][1])
        elif op[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += op[i][1]
        else:
            bag.sort()
            print(bag[0])
            bag.pop(0)
