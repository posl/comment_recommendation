def problem177_a():
    d,t,s = map(int, raw_input().split())
    if d <= s*t:
        print "Yes"
    else:
        print "No"
problem177_a()
