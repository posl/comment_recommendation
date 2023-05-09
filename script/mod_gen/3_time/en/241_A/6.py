def problem():
    a = map(int, raw_input().split())
    for i in range(3):
        a = [a[x] for x in a]
    print a[0]
problem()

if __name__ == '__main__':
    problem()