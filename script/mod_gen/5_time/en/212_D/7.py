def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append([int(i) for i in input().split()])
    output = []
    bag = []
    for i in range(n):
        if q[i][0] == 1:
            bag.append(q[i][1])
        elif q[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += q[i][1]
        elif q[i][0] == 3:
            output.append(min(bag))
            bag.remove(min(bag))
    for i in output:
        print(i)

if __name__ == '__main__':
    main()