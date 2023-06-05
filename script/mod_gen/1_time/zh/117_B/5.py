def is_polygon(n, data):
    max_len = max(data)
    sum_len = sum(data) - max_len
    if max_len < sum_len:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    is_polygon()