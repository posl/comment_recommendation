def get_max_value_baggage(baggage, boxes):
    #sort by weight so that we can use binary search
    baggage = sorted(baggage, key=lambda x: x[0])
    boxes = sorted(boxes)
    #dp[i][j] is the maximum value we can get by using the first i baggage and j boxes
    dp = [[0 for _ in range(len(boxes) + 1)] for _ in range(len(baggage) + 1)]
    for i in range(1, len(baggage) + 1):
        for j in range(1, len(boxes) + 1):
            #if the current box can hold the current baggage
            if boxes[j - 1] >= baggage[i - 1][0]:
                #we can either put the current baggage in the current box or not
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + baggage[i - 1][1])
            else:
                #we can't put the current baggage in the current box
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]

if __name__ == '__main__':
    get_max_value_baggage()