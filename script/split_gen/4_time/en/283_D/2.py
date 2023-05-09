def main():
    s = input()
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            j = stack.pop()
            if s[j+1:i].isalpha():
                print('No')
                return
    print('Yes')
    return
