def main():
    Q = int(input())
    bag = []
    for i in range(Q):
        query = input()
        if query[0] == '1':
            bag.append(int(query.split(' ')[1]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query.split(' ')[1])
        else:
            print(min(bag))
            bag.remove(min(bag))
main()
