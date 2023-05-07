def calculateInnerProduct(a,b):
    innerProduct = 0
    for i in range(len(a)):
        innerProduct += a[i]*b[i]
    return innerProduct
