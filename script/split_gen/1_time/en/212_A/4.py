def main():
    A, B = map(int, raw_input().split())
    if A > 0 and B == 0:
        print "Gold"
    elif A == 0 and B > 0:
        print "Silver"
    else:
        print "Alloy"
