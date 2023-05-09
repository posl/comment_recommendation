def main():
    # get input
    n, q = map(int, input().split())
    # make a list of lists to hold the trains
    trains = []
    # make a list to hold the car numbers
    car_nums = []
    # make a list to hold the car numbers that are connected to the rear
    rear_nums = []
    # make a list to hold the car numbers that are connected to the front
    front_nums = []
    # make a list to hold the car numbers that are connected to the rear and front
    both_nums = []
    # make a list to hold the car numbers that are not connected to the rear or front
    neither_nums = []
    # make a list to hold the car numbers that are connected to the rear and front
    both_nums = []
    # make a list to hold the car numbers that are not connected to the rear or front
    neither_nums = []
    # fill the trains list with n empty lists
    for i in range(n):
        trains.append([])
    # fill the car_nums list with the car numbers
    for i in range(n):
        car_nums.append(i+1)
    # fill the rear_nums list with the car numbers that are connected to the rear
    for i in range(n):
        rear_nums.append(i+1)
    # fill the front_nums list with the car numbers that are connected to the front
    for i in range(n):
        front_nums.append(i+1)
    # fill the both_nums list with the car numbers that are connected to the rear and front
    for i in range(n):
        both_nums.append(i+1)
    # fill the neither_nums list with the car numbers that are not connected to the rear or front
    for i in range(n):
        neither_nums.append(i+1)
    # make a list to hold the queries
    queries = []
    # fill the queries list with the queries
    for i in range(q):
        queries.append(list(map(int, input().split())))
    # process the queries
    for query in queries:
        # check the first value of the query
        if query[0] == 1:
            # make a list to hold the car numbers in the rear_nums list
            temp = []
            # make a list to hold the car numbers in the front_nums list
            temp2 = []
            # make a list to

if __name__ == '__main__':
    main()