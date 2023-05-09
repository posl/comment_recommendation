def main():
    # List of dishes
    dishes = []
    # List of times
    times = []
    # Number of dishes
    num_dishes = 5
    # Get input
    for i in range(0, num_dishes):
        dish = input()
        dishes.append(dish)
        # Calculate the time to serve each dish
        time = int(dish) // 10
        # If the time is not a multiple of 10, add 1
        if time % 10 != 0:
            time += 1
        times.append(time)
    # Get the maximum time
    max_time = max(times)
    # Get the index of the maximum time
    index = times.index(max_time)
    # Get the time to serve the last dish
    last_dish_time = dishes[index]
    # Calculate the total time
    total_time = last_dish_time + (max_time * 10)
    # Print the total time
    print(total_time)
main()

if __name__ == '__main__':
    main()