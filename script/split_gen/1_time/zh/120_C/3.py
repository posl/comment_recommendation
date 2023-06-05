def main():
    s = input()
    s = list(s)
    s.reverse()
    count = 0
    for i in range(0,len(s)-1):
        if s[i] == '0':
            count += 1
        elif s[i] == '1' and s[i+1] == '0':
            count += 1
    print(count)
