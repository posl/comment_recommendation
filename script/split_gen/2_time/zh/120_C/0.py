def main():
    s = input()
    n = len(s)
    r = s.count('0')
    b = n - r
    print(min(r,b)*2)
