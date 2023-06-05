def get_missing_number(str):
    for i in range(10):
        if str.find(str(i)) == -1:
            return i
