def find_missing_number(s):
    for i in range(1,10):
        if str(i) not in s:
            return i
