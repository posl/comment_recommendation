def missing_number(s):
    for i in range(0,10):
        if str(i) not in s:
            return i
