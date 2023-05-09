def check(p):
    for i in range(len(p)):
        if p[i] != p[len(p)-1-i]:
            return False
    return True
s = input()
