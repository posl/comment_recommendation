def get_min_time():
    dishes = [int(input()) for _ in range(5)]
    min_time = 0
    for dish in dishes:
        if dish % 10 != 0:
            min_time += (dish // 10 + 1) * 10
        else:
            min_time += dish
    return min_time - max([dish for dish in dishes if dish % 10 != 0])
print(get_min_time())

if __name__ == '__main__':
    get_min_time()