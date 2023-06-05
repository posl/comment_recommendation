def isArithmeticSequence(a1, a2, a3):
    if a3 - a2 == a2 - a1:
        return True
    else:
        return False
a1, a2, a3 = map(int, input().split())
