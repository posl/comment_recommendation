def main():
    #Read the input
    x, y = map(int, input().split())
    #Check if the team which is behind can turn the tables with a successful three-point goal
    if x > y:
        print("Yes") if ((x - y) > 2) else print("No")
    else:
        print("Yes") if ((y - x) > 2) else print("No")
