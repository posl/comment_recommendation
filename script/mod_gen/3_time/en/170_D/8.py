def main():
    # Read input
    N = int(input())
    A = list(map(int, input().split()))
    # Count the number of occurrences of each number
    # (use a dictionary for this)
    count = {}
    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    # Check which numbers are divisible by other numbers
    # (use a dictionary for this)
    div = {}
    for a in A:
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                if a in div:
                    div[a] = True
                elif i in count:
                    div[a] = True
                elif a//i in count:
                    div[a] = True
    # Count the result
    res = 0
    for a in A:
        if a not in div:
            res += count[a]
    print(res)

if __name__ == '__main__':
    main()