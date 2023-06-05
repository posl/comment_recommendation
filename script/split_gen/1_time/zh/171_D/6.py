def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    sum_a = sum(a)
    dic = {i:0 for i in range(1, 10**5+1)}
    for i in a:
        dic[i] += 1
    for b, c in bc:
        sum_a += (c-b)*dic[b]
        dic[c] += dic[b]
        dic[b] = 0
        print(sum_a)
