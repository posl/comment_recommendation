def main():
    s = raw_input()
    t = raw_input()
    if s + t[-1] == t:
        print "Yes"
    else:
        print "No"

if __name__ == '__main__':
    main()