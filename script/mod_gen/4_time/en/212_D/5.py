def main():
    n = int(input())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    bag = []
    for i in x:
        if i[0] == 1:
            bag.append(i[1])
        elif i[0] == 2:
            for j in range(len(bag)):
                bag[j] += i[1]
        else:
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()