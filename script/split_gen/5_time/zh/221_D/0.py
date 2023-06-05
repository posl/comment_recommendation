def main():
    n = int(input())
    a_b = []
    for _ in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[0])
    a_b.sort(key=lambda x: x[1])
    # print(a_b)
    a = [x[0] for x in a_b]
    b = [x[1] for x in a_b]
    # print(a)
    # print(b)
    a_b = []
    for i in range(n):
        if i == 0:
            a_b.append([a[i], b[i]])
        else:
            if a[i] == a[i-1]:
                a_b[-1][1] += b[i]
            else:
                a_b.append([a[i], b[i]])
    # print(a_b)
    b = [x[1] for x in a_b]
    # print(b)
    ans = []
    for i in range(1, n+1):
        ans.append(b.count(i))
    print(' '.join(map(str, ans)))
