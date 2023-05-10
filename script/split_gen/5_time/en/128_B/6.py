def main():
    restaurants = []
    for i in range(int(input())):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for restaurant in restaurants:
        print(restaurant[2])
