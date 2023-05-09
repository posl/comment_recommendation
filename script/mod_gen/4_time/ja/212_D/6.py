def main():
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    bag = []
    min_value = 0
    for p, x in query:
        if p == 1:
            bag.append(x - min_value)
        elif p == 2:
            min_value += x
        else:
            print(bag.pop() + min_value)

if __name__ == '__main__':
    main()