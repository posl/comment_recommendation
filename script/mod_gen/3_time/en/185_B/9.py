def main():
    battery_capacity, number_of_cafes, time_to_return_home = map(int, input().split())
    time_to_visit_cafe = []
    for i in range(number_of_cafes):
        time_to_visit_cafe.append(list(map(int, input().split())))
    battery_charge = battery_capacity
    current_time = 0
    for i in range(number_of_cafes):
        battery_charge -= (time_to_visit_cafe[i][0] - current_time)
        if battery_charge <= 0:
            print('No')
            return
        battery_charge += (time_to_visit_cafe[i][1] - time_to_visit_cafe[i][0])
        if battery_charge > battery_capacity:
            battery_charge = battery_capacity
        current_time = time_to_visit_cafe[i][1]
    battery_charge -= (time_to_return_home - current_time)
    if battery_charge <= 0:
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()