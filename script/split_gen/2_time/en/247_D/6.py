def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append([int(x) for x in input().split()])
    q1 = [x for x in q if x[0] == 1]
    q2 = [x for x in q if x[0] == 2]
    q2 = [x[1] for x in q2]
    q2.reverse()
    for i in range(len(q2)):
        q2[i] = [i, q2[i]]
    q2.reverse()
    q1.reverse()
    ans = []
    for i in range(len(q2)):
        while q2[i][1] > 0:
            if q1[-1][2] <= q2[i][1]:
                ans.append([q1[-1][1], q1[-1][2]])
                q2[i][1] -= q1[-1][2]
                q1.pop()
            else:
                ans.append([q1[-1][1], q2[i][1]])
                q1[-1][2] -= q2[i][1]
                q2[i][1] = 0
    ans.reverse()
    for i in ans:
        print(i[0] * i[1])
