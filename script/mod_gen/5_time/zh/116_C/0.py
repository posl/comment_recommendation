def min_watering(h):
    count = 0
    for i in range(len(h)):
        if h[i] == 0:
            continue
        elif i == len(h)-1:
            count += h[i]
        else:
            count += h[i]
            if h[i] <= h[i+1]:
                count += h[i]
            else:
                count += h[i+1]
    return count

if __name__ == '__main__':
    min_watering()