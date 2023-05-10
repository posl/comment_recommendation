def main():
    q = int(input())
    queries = [input().split() for _ in range(q)]
    bag = []
    min_value = 0
    for query in queries:
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            bag = [x + int(query[1]) for x in bag]
        else:
            min_value = min(bag)
            bag.remove(min_value)
            print(min_value)

if __name__ == '__main__':
    main()