def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Bad')
    elif s[1] == s[2] == s[3]:
        print('Bad')
    elif s[0] == s[1] == s[2]:
        print('Bad')
    elif s[0] == s[1] == s[3]:
        print('Bad')
    elif s[0] == s[2] == s[3]:
        print('Bad')
    else:
        print('Good')
