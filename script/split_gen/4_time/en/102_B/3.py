def main():
    # Get input here
    n = int(input())
    a = list(map(int, input().split()))
    # Calculate result here
    max_num = max(a)
    min_num = min(a)
    result = max_num - min_num
    # Print result here
    print(result)
main()
