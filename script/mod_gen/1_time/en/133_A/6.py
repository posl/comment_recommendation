def main():
    #Get the input
    N, A, B = map(int, input().split())
    #Calculate the minimum travel cost
    trainCost = N * A
    taxiCost = B
    minTravelCost = min(trainCost, taxiCost)
    #Print the minimum travel cost
    print(minTravelCost)

if __name__ == '__main__':
    main()