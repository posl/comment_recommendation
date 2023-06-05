def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    sum_a = sum(a)
    b = [0] * 100001
    for i in a:
        b[i] += 1
    for i in range(q):
        sum_a += (bc[i][1] - bc[i][0]) * b[bc[i][0]]
        b[bc[i][1]] += b[bc[i][0]]
        b[bc[i][0]] = 0
        print(sum_a)
