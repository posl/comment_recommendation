def splitNum(n):
    nStr = str(n)
    nLen = len(nStr)
    maxProduct = 0
    for i in range(1,nLen):
        num1 = nStr[0:i]
        num2 = nStr[i:nLen]
        product = int(num1)*int(num2)
        if product > maxProduct:
            maxProduct = product
    return maxProduct
