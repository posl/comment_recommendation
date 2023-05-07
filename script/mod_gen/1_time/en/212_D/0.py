def main():
    Q = int(input())
    bag = []
    for _ in range(Q):
        p, x = map(int, input().split())
        if p == 1:
            bag.append(x)
        elif p == 2:
            bag = [i + x for i in bag]
        else:
            bag = sorted(bag)
            print(bag.pop(0))

if __name__ == '__main__':
    main()