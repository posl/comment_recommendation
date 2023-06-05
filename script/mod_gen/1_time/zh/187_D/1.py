def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append([int(x) for x in input().split()])
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    # print(AB)
    count = 0
    for i in range(N):
        if i % 2 == 0:
            count += AB[i][0]
        else:
            count -= AB[i][1]
    print(count)

if __name__ == '__main__':
    solve()