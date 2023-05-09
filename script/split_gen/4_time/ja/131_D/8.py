def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[1])
    now = 0
    for i in range(N):
        now += AB[i][0]
        if now > AB[i][1]:
            print('No')
            exit()
    print('Yes')
