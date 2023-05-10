def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    a_sum = sum(a)
    for i in range(q):
        if query[i][0] == 1:
            print(a_sum + n * query[i][1])
        elif query[i][0] == 2:
            a_sum += query[i][2]
        elif query[i][0] == 3:
            print(a[query[i][1] - 1])
