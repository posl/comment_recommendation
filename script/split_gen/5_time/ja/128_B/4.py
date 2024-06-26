def main():
    N = int(input())
    restaurants = []
    for i in range(N):
        S, P = input().split()
        restaurants.append((S, int(P), i + 1))
    restaurants.sort(key=lambda x: x[1], reverse=True)
    restaurants.sort(key=lambda x: x[0])
    for r in restaurants:
        print(r[2])
