def main():
    # Get input here
    N, S, D = map(int, input().strip().split())
    spells = [tuple(map(int, input().strip().split())) for _ in range(N)]
    # Calculate result here
    result = 'No'
    for x, y in spells:
        if x < S and y > D:
            result = 'Yes'
            break
    # Print result here
    print(result)
main()
