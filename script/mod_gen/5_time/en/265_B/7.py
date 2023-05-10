def problem265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]
    current_time = t
    current_room = 1
    for i in range(m):
        current_time = current_time - (xy[i][0] - current_room)
        current_room = xy[i][0]
        if current_time <= 0:
            print("No")
            return
        current_time = current_time + xy[i][1]
        if current_time > t:
            current_time = t
    current_time = current_time - (n - current_room)
    if current_time <= 0:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    problem265_b()