def getNumOfSquares(h, w, r, c):
    numOfSquares = 0
    if r > 1:
        numOfSquares += 1
    if r < h:
        numOfSquares += 1
    if c > 1:
        numOfSquares += 1
    if c < w:
        numOfSquares += 1
    return numOfSquares

if __name__ == '__main__':
    getNumOfSquares()