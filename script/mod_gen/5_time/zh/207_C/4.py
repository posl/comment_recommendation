def main():
    #get the number of the intervals
    n = int(input())
    #get the intervals
    tlr = [list(map(int, input().split())) for _ in range(n)]
    #calculate the number of the intersection of the intervals
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            #if the intervals are the same type
            if tlr[i][0] == tlr[j][0]:
                #if the intervals are closed
                if tlr[i][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                        ans += 1
                #if the intervals are half-closed
                elif tlr[i][0] == 2:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2] or tlr[j][1] < tlr[i][1] < tlr[j][2]:
                        ans += 1
                #if the intervals are half-open
                elif tlr[i][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2] or tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        ans += 1
                #if the intervals are open
                else:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2] or tlr[j][1] < tlr[i][1] < tlr[j][2]:
                        ans += 1
            #if the intervals are different type
            else:
                #if the intervals are closed and half-closed
                if tlr[i][0] == 1:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2] or tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        ans += 1
                #if the intervals are closed and half-open
                elif tlr[i][0] == 2:
                    if tlr[i][1] <= tlr[j][1] <= tlr

if __name__ == '__main__':
    main()