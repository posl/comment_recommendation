def main():
    #Read input
    A, B, W = map(int, input().split())
    #Initialize variables
    min = 1000
    max = 0
    #Check every possible weight
    for i in range(1, 1001):
        #If the weight is within the range
        if i * A <= W * 1000 and i * B >= W * 1000:
            #If the weight is smaller than the current minimum
            if i < min:
                #Update the minimum
                min = i
            #If the weight is larger than the current maximum
            if i > max:
                #Update the maximum
                max = i
    #If no weight was found
    if min == 1000:
        #Output UNSATISFIABLE
        print("UNSATISFIABLE")
    else:
        #Output the minimum and maximum
        print(min, max)
