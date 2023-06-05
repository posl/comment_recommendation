def main():
    n = int(input())
    s = input()
    for i in range(0,n):
        if i % 2 == 0:
            print(s[i],end='')
        else:
            if s[i] == '"':
                print('"',end='')
            else:
                print('.',end='')
    print()
