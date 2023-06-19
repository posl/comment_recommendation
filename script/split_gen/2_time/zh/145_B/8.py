def check(string):
    length = len(string)
    if length % 2 == 1:
        return False
    else:
        half = length // 2
        if string[:half] == string[half:]:
            return True
        else:
            return False
