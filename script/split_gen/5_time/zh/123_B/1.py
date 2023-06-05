def main():
    dishes = []
    for i in range(5):
        dishes.append(int(input()))
    min_time = 100000000000
    for i in range(5):
        if dishes[i] < min_time:
            min_time = dishes[i]
    for i in range(5):
        if dishes[i] % 10 != 0:
            dishes[i] = dishes[i] + 10 - dishes[i] % 10
    print(dishes[0] + dishes[1] + dishes[2] + dishes[3] + dishes[4])
