def main():
    n = int(input())
    s = input()
    result = ''
    flag = False
    for i in range(n):
        if s[i] == '"':
            if flag:
                flag = False
            else:
                flag = True
        if s[i] == ',' and flag:
            result += s[i]
        elif s[i] == ',':
            result += '.'
        else:
            result += s[i]
    print(result)
