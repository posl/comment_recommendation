def main():
    # Get input here
    input_list = list(map(int, input().split()))
    # Calculate the ans
    ans = len(set(input_list))
    # Print the ans
    print(ans)
main()
