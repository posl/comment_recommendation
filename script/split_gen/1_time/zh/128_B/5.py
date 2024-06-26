def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        city, score = input().split()
        restaurants.append((city, int(score), i + 1))
    restaurants.sort(key=lambda x: x[1], reverse=True)
    restaurants.sort(key=lambda x: x[0])
    for restaurant in restaurants:
        print(restaurant[2])
