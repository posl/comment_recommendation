def main():
    # Get input here
    N = int(input())
    # Calculate result here
    result = 0
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            result += 1
            N = N // i
            while N % i == 0:
                N = N // i
    if N != 1:
        result += 1
    # Print output here
    print(result)
main()
