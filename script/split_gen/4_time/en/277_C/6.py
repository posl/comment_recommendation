def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[0])
    AB.sort(key=lambda x:x[1])
    print(AB[-1][1])
