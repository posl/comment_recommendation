def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    for z in range(x+1, y+1):
        if max(x_list) < z and min(y_list) >= z:
            print("No War")
            return
    print("War")
main()
