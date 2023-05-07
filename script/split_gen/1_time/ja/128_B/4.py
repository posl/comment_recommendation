def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        s, p = input().split()
        restaurants.append([s, int(p), i+1])
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(restaurants[i][2])
