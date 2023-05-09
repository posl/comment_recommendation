def max_move(n, heights):
    max_count = 0
    count = 0
    for i in range(n-1):
        if heights[i] >= heights[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

if __name__ == '__main__':
    max_move()