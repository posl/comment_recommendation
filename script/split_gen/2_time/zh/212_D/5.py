def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int,input().split())))
    bag = []
    for i in range(n):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        elif q[i][0] == 3:
            bag.sort()
            print(bag[0])
            bag.pop(0)
