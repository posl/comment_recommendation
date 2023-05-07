def findSnukeNum(K):
    # 1 is a snuke number
    snukeNums = [1]
    # Keep track of the next snuke number to add
    nextNum = 2
    # Keep track of the sum of the digits of the next snuke number
    nextSum = 2
    # Keep track of the sum of the digits of the last snuke number added
    lastSum = 1
    # Keep track of the last snuke number added
    lastNum = 1
    # Keep track of the sum of the digits of the last snuke number added
    lastSum = 1
    # Keep track of the sum of the digits of the next snuke number to add
    nextSum = 2
    # Keep track of the next snuke number to add
    nextNum = 2
    # Keep track of the sum of the digits of the last snuke number added
    lastSum = 1
    # Keep track of the last snuke number added
    lastNum = 1
    # While we have not found K snuke numbers
    while len(snukeNums) < K:
        # If the next snuke number is less than the last snuke number added
        if nextNum < lastNum:
            # Add the next snuke number to the list
            snukeNums.append(nextNum)
            # Increase the sum of the digits of the next snuke number
            nextSum += 1
            # Increase the next snuke number
            nextNum += 1
        # If the next snuke number is greater than the last snuke number added
        elif nextNum > lastNum:
            # Add the next snuke number to the list
            snukeNums.append(nextNum)
            # Increase the sum of the digits of the next snuke number
            nextSum += 1
            # Increase the next snuke number
            nextNum += 1
        # If the next snuke number is equal to the last snuke number added
        else:
            # If the sum of the digits of the next snuke number is greater than the sum of the digits of the last snuke number added
            if nextSum > lastSum:
                # Add the next snuke number to the list
                snukeNums.append
