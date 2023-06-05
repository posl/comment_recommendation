def findAB(X):
    for A in range(1, 1001):
        for B in range(-1000, 0):
            if A ** 5 - B ** 5 == X:
                return A, B
X = int(input())
A, B = findAB(X)
print(A, B)

if __name__ == '__main__':
    findAB()