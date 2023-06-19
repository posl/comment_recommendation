def check(x):
    if x[0] in ['H','D','C','S'] and x[1] in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        return True
    else:
        return False
n = input()
s = [raw_input() for i in range(n)]

if __name__ == '__main__':
    check()