def main():
    p = input()
    p = p.split()
    s = ''
    for i in p:
        s += chr(int(i) + 96)
    print(s)
