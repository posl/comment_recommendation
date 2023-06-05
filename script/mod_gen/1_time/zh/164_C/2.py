def main():
    # Get the number of times to draw
    num_draws = int(input())
    # Create a set to store the items
    items = set()
    # Iterate through the draws
    for i in range(num_draws):
        # Get the item from the draw
        item = input()
        # Add the item to the set
        items.add(item)
    # Print the number of unique items
    print(len(items))

if __name__ == '__main__':
    main()