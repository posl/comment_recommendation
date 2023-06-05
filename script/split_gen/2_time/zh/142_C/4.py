def check_ride_roller_coaster(n,k,h):
    count=0
    for i in h:
        if i>=k:
            count+=1
    return count
