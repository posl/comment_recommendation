def main():
    s = input()
    flag = True
    if s.islower():
        flag = False
    if s.isupper():
        flag = False
    if flag:
        print('Yes')
    else:
        print('No')
