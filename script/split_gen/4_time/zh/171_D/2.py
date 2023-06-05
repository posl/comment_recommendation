def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    bc = [input().split() for _ in range(q)]
    b = [int(i[0]) for i in bc]
    c = [int(i[1]) for i in bc]
    print(sum(a))
    for i in range(q):
        print(sum(a) - a.count(b[i]) * (b[i] - c[i]))
