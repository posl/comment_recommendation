def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if s[i] == '..........':
            s[i] = '..........'
        elif s[i] == '##########':
            s[i] = '##########'
        else:
            s[i] = s[i][1:9]
    for i in range(10):
        print(s[i])
