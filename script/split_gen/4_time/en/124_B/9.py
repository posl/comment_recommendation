def main():
    # read the input
    N = int(input())
    H = list(map(int, input().split()))
    
    # initialize the counter
    count = 0
    
    # loop through the list of heights
    for i in range(N):
        # check if the current height is the highest
        if H[i] == max(H[:i+1]):
            # if so, increment the counter
            count += 1
    
    # print the result
    print(count)
