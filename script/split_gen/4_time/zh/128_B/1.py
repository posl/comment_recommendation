def main():
    n = int(input())
    restaurant = []
    for i in range(n):
        s, p = input().split()
        restaurant.append([s, int(p), i+1])
    restaurant.sort(key=lambda x: (x[0], -x[1]))
    for r in restaurant:
        print(r[2])
