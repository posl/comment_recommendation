def main():
    s = input()
    n = len(s)
    if s == s[::-1] and s[:int((n-1)/2)] == s[:int((n-1)/2):-1] and s[int((n+3)/2)-1:] == s[int((n+3)/2)-1::-1]:
        print('Yes')
    else:
        print('No')
