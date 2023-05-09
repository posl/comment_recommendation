def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    # print(AB)
    AB.reverse()
    # print(AB)
    # print(X)
    count = 0
    time = 0
    for i in range(N):
        if time + AB[i][1] <= X:
            count += 1
            time += AB[i][1]
        else:
            time += AB[i][1]
    # print(count)
    for i in range(N):
        time += AB[i][0]
        count += 1
        if time > X:
            count -= 1
            break
    print(count)
