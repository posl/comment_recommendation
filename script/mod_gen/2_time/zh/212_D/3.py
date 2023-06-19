def main():
    N = int(input())
    bag = []
    for i in range(N):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            bag = [x+int(query[1]) for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()