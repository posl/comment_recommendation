def check_double_string(n, s):
    if n % 2 != 0:
        return False
    half = int(n/2)
    if s[0:half] == s[half:n]:
        return True
    else:
        return False
n = int(input())
s = input()

if __name__ == '__main__':
    check_double_string()