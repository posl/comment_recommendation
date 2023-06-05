def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[1])
    for i in range(N):
        if sum(map(lambda x:x[0], AB[:i+1])) > AB[i][1]:
            print('No')
            return
    print('Yes')
