def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: (x[1],x[0]))
    count = 0
    reward = 0
    for i in range(N):
        if count >= M:
            break
        if count + AB[i][0] <= M:
            count += AB[i][0]
            reward += AB[i][1]
        else:
            reward += AB[i][1]*(M-count)
            count = M
    print(reward)

if __name__ == '__main__':
    main()