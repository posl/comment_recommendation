def printSequences(n, m, sequence):
    if n == 0:
        print(sequence)
        return
    if n > 0:
        for i in range(1, m+1):
            printSequences(n-1, m, sequence + str(i) + " ")
    return
n, m = map(int, input().split())
printSequences(n, m, "")

if __name__ == '__main__':
    printSequences()