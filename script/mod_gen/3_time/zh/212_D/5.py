def main():
    # 读入数据
    q = int(input())
    bag = []
    for i in range(q):
        line = input().split()
        if line[0] == '1':
            bag.append(int(line[1]))
        elif line[0] == '2':
            bag = [x + int(line[1]) for x in bag]
        elif line[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()