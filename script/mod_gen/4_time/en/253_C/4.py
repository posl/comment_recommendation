def main():
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    s = []
    for q in queries:
        if q[0] == 1:
            s.append(q[1])
        elif q[0] == 2:
            for _ in range(min(q[2], s.count(q[1]))):
                s.remove(q[1])
        else:
            print(max(s) - min(s))
    return

if __name__ == '__main__':
    main()