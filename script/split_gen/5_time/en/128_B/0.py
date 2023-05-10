def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        P = int(P)
        restaurants.append([i+1, S, P])
    restaurants.sort(key=lambda x: x[0])
    restaurants.sort(key=lambda x: x[2], reverse=True)
    restaurants.sort(key=lambda x: x[1])
    for i in range(N):
        print(restaurants[i][0])
