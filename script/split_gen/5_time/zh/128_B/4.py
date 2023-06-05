def main():
    n = int(input())
    # restaurants = []
    # for i in range(n):
    #     restaurants.append(input().split())
    restaurants = [input().split() for i in range(n)]
    restaurants.sort(key=lambda x: x[0])
    restaurants.sort(key=lambda x: int(x[1]), reverse=True)
    for i in range(n):
        print(restaurants[i][2])
