def main():
    D, T, S = map(int, raw_input().split())
    if D <= T * S:
        print "Yes"
    else:
        print "No"
main()
