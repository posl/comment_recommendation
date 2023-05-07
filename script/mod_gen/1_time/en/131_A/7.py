def check_hard_to_enter(s):
    for i in range(3):
        if s[i] == s[i+1]:
            return True
    return False
s = raw_input()

if __name__ == '__main__':
    check_hard_to_enter()