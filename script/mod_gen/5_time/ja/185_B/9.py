def calc_battery_capacity(N, M, T, cafe):
    battery_capacity = N
    battery = N
    for cafe_time in cafe:
        battery -= (cafe_time[0] - cafe_time[1])
        if battery <= 0:
            return False
        battery += (cafe_time[1] - cafe_time[0])
        if battery > battery_capacity:
            battery = battery_capacity
    battery -= (T - cafe[-1][1])
    if battery <= 0:
        return False
    return True

if __name__ == '__main__':
    calc_battery_capacity()