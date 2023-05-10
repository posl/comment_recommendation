def main():
    # Get the input
    n = int(input())
    a = list(map(int, input().split()))
    # Initialize the output
    b = []
    # Check if there is a good set of choices
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            b.append(i+1)
            for j in range(1, i//2+1):
                a[j] = 1 - a[j]
            if i == 0:
                break
    # Print the output
    if sum(a) == 0:
        print(len(b))
        for i in range(len(b)):
            print(b[i])
    else:
        print(-1)
