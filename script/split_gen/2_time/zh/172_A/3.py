def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    # print(a)
    # print(bc)
    s = sum(a)
    for b, c in bc:
        s += (c - b) * a.count(b)
        print(s)
        a = [c if x == b else x for x in a]
