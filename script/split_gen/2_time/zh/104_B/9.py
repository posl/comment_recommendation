def main():
    s = input()
    if s[0] != 'A':
        print("WA")
        return
    if s[2:-1].count('C') != 1:
        print("WA")
        return
    if s.replace('A', '').replace('C', '').islower():
        print("AC")
        return
    print("WA")
