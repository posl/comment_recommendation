def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    time = 0
    for ab in AB:
        time += ab[0]
        if time > ab[1]:
            print('No')
            return
    print('Yes')
    return
