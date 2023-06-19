def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print('1')
