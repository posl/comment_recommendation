def main():
    #Get the number of trees and the number of trees to decorate
    N,K = map(int,input().split())
    #Get the height of each tree
    H = [int(input()) for i in range(N)]
    #Sort the heights
    H.sort()
    #Set the minimum difference to a large number
    min_diff = 10**10
    #Loop through the heights
    for i in range(N-K+1):
        #Calculate the difference between the first and last trees to decorate
        diff = H[i+K-1] - H[i]
        #If the difference is less than the current minimum difference
        if diff < min_diff:
            #Update the minimum difference
            min_diff = diff
    #Output the minimum difference
    print(min_diff)
