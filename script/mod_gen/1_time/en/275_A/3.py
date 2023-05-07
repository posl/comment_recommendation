def main():
    # Get the number of bridges
    num_bridges = int(input())
    # Get the heights of the bridges
    bridge_heights = list(map(int, input().split()))
    # Print the number of the highest bridge
    print(bridge_heights.index(max(bridge_heights)) + 1)

if __name__ == '__main__':
    main()