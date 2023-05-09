def problem():
    # Get input
    input = raw_input()
    input = input.split()
    # Check input
    if len(input) != 2:
        print "Error: Please provide two integers"
        return
    try:
        l = int(input[0])
        r = int(input[1])
    except:
        print "Error: Please provide two integers"
        return
    # Check input
    if l > r:
        print "Error: L should be smaller than R"
        return
    if l < 1 or r < 1 or l > 7 or r > 7:
        print "Error: L and R should be between 1 and 7"
        return
    # Get string
    s = "atcoder"
    # Print result
    print s[l-1:r]
problem()
