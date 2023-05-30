def replace_all(target, char, replace):
    return target.replace(char, replace)
s = input()
print(replace_all(s, s, 'x'))
