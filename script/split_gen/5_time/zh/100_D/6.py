def main():
    N,M = map(int,input().split())
    cake = []
    for i in range(N):
        cake.append(list(map(int,input().split())))
    if N == 1:
        print(abs(cake[0][0]) + abs(cake[0][1]) + abs(cake[0][2]))
        return
    if M == 0:
        print(0)
        return
    if M == 1:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 2:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 3:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 4:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 5:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 6:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 7:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 8:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
    if M == 9:
        print(max(abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2]) for i in range(N)))
        return
