def main():
    # Read the input
    x, y = map(int, input().split())
    # Calculate the answer
    if x == y:
        answer = x
    elif x != y:
        answer = 3 - x - y
    # Print the answer
    print(answer)
