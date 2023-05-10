def check_duplication(names):
    for i in range(0, len(names)-1):
        for j in range(i+1, len(names)):
            if names[i] == names[j]:
                return True
    return False
