def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    war = False
    for z in range(x+1, y+1):
        if all([x < z for x in x_list]) and all([z <= y for y in y_list]):
            war = True
            break
    print("War" if war else "No War")
