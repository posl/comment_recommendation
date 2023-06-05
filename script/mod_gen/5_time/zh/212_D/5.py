def main():
    q = int(input())
    bag = []
    for i in range(q):
        line = input().split()
        if line[0] == "1":
            bag.append(int(line[1]))
        elif line[0] == "2":
            for j in range(len(bag)):
                bag[j] += int(line[1])
        elif line[0] == "3":
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()