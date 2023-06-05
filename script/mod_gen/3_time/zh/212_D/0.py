def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    q.reverse()
    bag = []
    for i in range(len(q)):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        elif q[i][0] == 3:
            print(bag.pop(bag.index(min(bag))))

if __name__ == '__main__':
    main()