def find_unique_char(string):
    ans = -1
    for i in range(len(string)):
        if string.rfind(string[i]) == i and string.find(string[i]) == i:
            ans = string[i]
            break
    return ans
