def main():
    n = int(input())
    restaurant_list = [input().split() for _ in range(n)]
    restaurant_list = [[restaurant_list[i][0], int(restaurant_list[i][1]), i+1] for i in range(n)]
    restaurant_list.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurant_list:
        print(restaurant[2])
