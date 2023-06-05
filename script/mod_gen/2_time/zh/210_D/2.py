def get_max_color_count(candies, k):
    max_color_count = 0
    for i in range(0, len(candies) - k + 1):
        color_count = len(set(candies[i:i+k]))
        if color_count > max_color_count:
            max_color_count = color_count
    return max_color_count

if __name__ == '__main__':
    get_max_color_count()