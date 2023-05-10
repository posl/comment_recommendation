def judge(str):
    while True:
        str = str.replace('()', '')
        if str == '':
            return True
        elif str == str.replace('()', ''):
            return False
s = input()
