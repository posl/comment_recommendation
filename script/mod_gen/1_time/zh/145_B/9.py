def main():
    n = input()
    s = raw_input()
    if s[0:n/2] == s[n/2:n]:
        print "Yes"
    else:
        print "No"

if __name__ == '__main__':
    main()