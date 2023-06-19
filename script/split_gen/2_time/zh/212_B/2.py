def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print('Weak')
    else:
        for i in range(3):
            if (int(s[i])+1)%10 != int(s[i+1]):
                print('Strong')
                break
        else:
            print('Weak')
