def main():
    s = input()
    if len(s) == len(set(s)) and s.islower() == False and s.isupper() == False:
        print('Yes')
    else:
        print('No')
