def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        restaurants.append(input().split())
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(n):
        print(restaurants[i][2])
