def main():
    n = int(input())
    q = [list(map(int,input().split())) for _ in range(n)]
    bag = []
    for i in range(n):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        else:
            print(min(bag))
            bag.remove(min(bag))
