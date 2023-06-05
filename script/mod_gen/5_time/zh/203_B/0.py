def sum_room_number(n,k):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            sum += i*100 + j
    return sum

if __name__ == '__main__':
    sum_room_number()