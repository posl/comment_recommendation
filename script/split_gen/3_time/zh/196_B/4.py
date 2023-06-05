def round_number(x):
    # Write your code here.
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if '.' in x:
        x = x.split('.')
        if int(x[1][0]) >= 5:
            return int(x[0])+1
        else:
            return int(x[0])
    else:
        return int(x)
