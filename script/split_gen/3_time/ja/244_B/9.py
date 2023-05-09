def main():
    N = int(input())
    T = input()
    #print(N, T)
    x = 0
    y = 0
    #東西南北の順に入れておく
    #東を向いているときは1
    #南を向いているときは2
    #西を向いているときは3
    #北を向いているときは4
    direction = 1
    for i in range(N):
        if T[i] == 'S':
            if direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            elif direction == 4:
                y += 1
        elif T[i] == 'R':
            if direction == 4:
                direction = 1
            else:
                direction += 1
    print(x, y)
