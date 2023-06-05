def solve(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return -1
print(solve(input()))
