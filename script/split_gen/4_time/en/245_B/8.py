def getSmallestNonNegativeIntegerNotInSequence(sequence):
    sortedSequence = sorted(sequence)
    smallestNonNegativeIntegerNotInSequence = 0
    for number in sortedSequence:
        if number <= smallestNonNegativeIntegerNotInSequence:
            smallestNonNegativeIntegerNotInSequence += 1
    return smallestNonNegativeIntegerNotInSequence
sequence = list(map(int, input().split()))
print(getSmallestNonNegativeIntegerNotInSequence(sequence))
