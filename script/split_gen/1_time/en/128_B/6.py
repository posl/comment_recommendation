def main():
    N = int(input())
    restaurants = [input().split() for _ in range(N)]
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(N):
        print(restaurants[i][2])
