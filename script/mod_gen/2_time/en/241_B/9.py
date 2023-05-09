def main():
    # Get the number of noodles and the number of days.
    n, m = map(int, input().split())
    # Get the lengths of the noodles.
    a = list(map(int, input().split()))
    # Get the lengths of the noodles that Takahashi wants to eat.
    b = list(map(int, input().split()))
    # Sort the lengths of the noodles in ascending order.
    a.sort()
    # Sort the lengths of the noodles that Takahashi wants to eat in ascending order.
    b.sort()
    # Set the number of the noodles that Takahashi has eaten to 0.
    eaten = 0
    # For each day...
    for i in range(m):
        # If the number of the noodles that Takahashi has eaten is greater than or equal to the number of the noodles...
        if eaten >= n:
            # Print No.
            print("No")
            # Exit the program.
            exit()
        # If the length of the noodle that Takahashi wants to eat is less than the length of the noodle that Takahashi has eaten...
        if b[i] < a[eaten]:
            # Print No.
            print("No")
            # Exit the program.
            exit()
        # If the length of the noodle that Takahashi wants to eat is greater than the length of the noodle that Takahashi has eaten...
        while b[i] > a[eaten]:
            # Increment the number of the noodles that Takahashi has eaten by 1.
            eaten += 1
            # If the number of the noodles that Takahashi has eaten is greater than or equal to the number of the noodles...
            if eaten >= n:
                # Print No.
                print("No")
                # Exit the program.
                exit()
    # Print Yes.
    print("Yes")

if __name__ == '__main__':
    main()