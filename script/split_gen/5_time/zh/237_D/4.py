def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n-1):
        if s[i] == 'L':
            a.insert(0,i+2)
        else:
            a.append(i+2)
    for i in a:
        print(i,end=' ')
    print('0')
