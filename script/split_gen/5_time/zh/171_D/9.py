def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for _ in range(q):
        bc.append(list(map(int, input().split())))
    sum_a = sum(a)
    for i in range(q):
        sum_a += (bc[i][1] - bc[i][0]) * a.count(bc[i][0])
        print(sum_a)
        a = [bc[i][1] if x == bc[i][0] else x for x in a]
