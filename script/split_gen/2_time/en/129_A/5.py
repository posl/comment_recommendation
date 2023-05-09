def min_flight_time():
    flight_time = list(map(int, input().split()))
    return sum(flight_time) - max(flight_time)
