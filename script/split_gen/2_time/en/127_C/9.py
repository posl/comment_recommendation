def main():
    #N and M
    N, M = map(int, input().split())
    #List of L_i and R_i
    LR = [list(map(int, input().split())) for _ in range(M)]
    #Sort the list of L_i and R_i
    LR.sort()
    #The number of ID cards that allow us to pass all the gates alone
    count = 0
    #The maximum of the L_i
    maxL = 0
    #The minimum of the R_i
    minR = N
    #Check the list of L_i and R_i
    for i in range(M):
        #Update the maximum of the L_i
        maxL = max(maxL, LR[i][0])
        #Update the minimum of the R_i
        minR = min(minR, LR[i][1])
        #Check if the maximum of the L_i is less than the minimum of the R_i
        if maxL <= minR:
            #Update the number of ID cards that allow us to pass all the gates alone
            count += 1
    #Print the number of ID cards that allow us to pass all the gates alone
    print(count)
