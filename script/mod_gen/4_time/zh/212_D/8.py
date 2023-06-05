def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(input().split())
    bag = []
    for i in range(n):
        if q[i][0] == '1':
            bag.append(int(q[i][1]))
        elif q[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(q[i][1])
        elif q[i][0] == '3':
            bag.sort()
            print(bag[0])
            bag.pop(0)

if __name__ == '__main__':
    main()