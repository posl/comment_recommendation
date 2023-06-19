def problem283_b():
    n = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())
    for i in range(q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            a[query[1] - 1] = query[2]
        else:
            print(a[query[1] - 1])

if __name__ == '__main__':
    problem283_b()