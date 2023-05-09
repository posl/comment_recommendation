def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    # Sort the ladders by the second element (the higher floor)
    ladders.sort(key=lambda x: x[1])
    # The highest floor that Takahashi can reach
    highest_floor = 1
    # For each ladder
    for i in range(n):
        # If the ladder's lower floor is higher than the current highest floor
        if ladders[i][0] > highest_floor:
            # Then he can't reach the higher floor using the ladder
            continue
        # Otherwise, update the highest floor
        highest_floor = ladders[i][1]
    # Print the highest floor that Takahashi can reach
    print(highest_floor)

if __name__ == '__main__':
    main()