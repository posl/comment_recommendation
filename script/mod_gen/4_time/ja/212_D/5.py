def main():
    q = int(input())
    l = []
    for i in range(q):
        l.append(list(map(int, input().split())))
    l.reverse()
    bag = []
    for i in range(q):
        if l[i][0] == 1:
            bag.append(l[i][1])
        elif l[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += l[i][1]
        else:
            bag.sort()
            print(bag.pop())

if __name__ == '__main__':
    main()