def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    a_b = []
    for i in range(M):
        a_b.append([a[i], b[i]])
    a_b.sort()
    a = []
    b = []
    for i in range(M):
        a.append(a_b[i][0])
        b.append(a_b[i][1])
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    ans = 0
    for i in range(len(a)):
        ans += (b[i] - a[i] - 1)
    print(ans)
