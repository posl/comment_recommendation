def sum_of_rooms(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            room = i*100+j
            sum += room
    return sum
