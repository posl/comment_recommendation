def main():
    n = int(input())
    a = []
    for _ in range(n):
        q = list(map(int, input().split()))
        if q[0] == 1:
            a.append(q[1])
        elif q[0] == 2:
            for _ in range(min(q[2], a.count(q[1]))):
                a.remove(q[1])
        else:
            print(max(a) - min(a))

if __name__ == '__main__':
    main()