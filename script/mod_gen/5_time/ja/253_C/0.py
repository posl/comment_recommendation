def main():
    q = int(input())
    s = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
        elif query[0] == 2:
            for i in range(query[1]):
                if query[1] == 0:
                    break
                if s.count(query[1]) >= query[2]:
                    s.remove(query[1])
        else:
            print(max(s) - min(s))

if __name__ == '__main__':
    main()