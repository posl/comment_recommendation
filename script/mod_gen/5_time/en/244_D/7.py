def main():
    # Take input Here and Call solution function
    colors = list(map(str, input().strip().split()))
    goals = list(map(str, input().strip().split()))
    if colors[0] == goals[0] and colors[1] == goals[1] and colors[2] == goals[2]:
        print("Yes")
    else:
        print("No")
    pass

if __name__ == '__main__':
    main()