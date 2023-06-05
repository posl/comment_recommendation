def main():
    q = int(input())
    query_list = []
    for i in range(q):
        query_list.append(input().split())
    bag = []
    for i in range(q):
        if query_list[i][0] == '1':
            bag.append(int(query_list[i][1]))
        elif query_list[i][0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query_list[i][1])
        else:
            min = bag[0]
            for j in range(len(bag)):
                if min > bag[j]:
                    min = bag[j]
            print(min)
            bag.remove(min)

if __name__ == '__main__':
    main()