def main():
    q = int(input())
    a = []
    for i in range(q):
        a.append(list(map(int, input().split())))
    ret = []
    bag = []
    for i in range(q):
        if a[i][0] == 1:
            bag.append(a[i][1])
        elif a[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += a[i][1]
        else:
            ret.append(min(bag))
            bag.remove(min(bag))
    for i in range(len(ret)):
        print(ret[i])

if __name__ == '__main__':
    main()