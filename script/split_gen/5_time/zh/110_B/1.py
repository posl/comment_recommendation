def main():
    n, m, x, y = map(int, input().split())
    x_city = list(map(int, input().split()))
    y_city = list(map(int, input().split()))
    for z in range(x+1, y+1):
        if max(x_city) < z <= min(y_city):
            print("No War")
            return
    print("War")
