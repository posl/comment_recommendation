def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((i+1, s, int(p)))
    restaurants.sort(key=lambda x: (x[1], -x[2]))
    for restaurant in restaurants:
        print(restaurant[0])
