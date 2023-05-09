def check_battery(battery, start, end):
    for i in range(start, end):
        battery -= 1
        if battery <= 0:
            return False
        if i % 1 == 0:
            battery += 1
            if battery > N:
                battery = N
    return True
N, M, T = map(int, input().split())
battery = N
start = 0
for i in range(M):
    A, B = map(int, input().split())
    if not check_battery(battery, start, A):
        print("No")
        exit()
    battery = check_battery(battery, A, B)
    start = B
