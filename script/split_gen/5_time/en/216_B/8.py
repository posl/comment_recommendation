def main():
    # Get the number of people
    n = int(input())
    # Create a list to store the names
    names = []
    # Get the names
    for i in range(n):
        names.append(input())
    # Check if there are any duplicates
    if len(names) != len(set(names)):
        print("Yes")
    else:
        print("No")
