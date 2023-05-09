def problems132_c():
    # Get input
    n = int(input())
    d = list(map(int, input().split()))
    # Sort list
    d.sort()
    # Get median
    median = d[int(n/2)]
    # Get result
    result = d[int(n/2)] - d[int(n/2)-1]
    # Print result
    print(result)

if __name__ == '__main__':
    problems132_c()