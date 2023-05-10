def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    q3 = []
    for i in range(n):
        if q[i][0] == 3:
            q3.append(i)
    q1 = []
    for i in range(n):
        if q[i][0] == 1:
            q1.append(q[i][1])
    q2 = []
    for i in range(n):
        if q[i][0] == 2:
            q2.append(q[i][1])
    q2sum = sum(q2)
    q2sum2 = 0
    for i in range(n):
        if q[i][0] == 3:
            print(q1[i] + q2sum - q2sum2)
            q2sum2 += q1[i]
