def get_missing_number(s):
    for i in range(10):
        if str(i) not in s:
            return i
