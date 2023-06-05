def room_number_sum(n, k):
    room_sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            room_sum += int(str(i) + '0' + str(j))
    return room_sum
