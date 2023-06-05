def main():
    s = input()
    k = int(input())
    l = len(s)
    for i in range(k):
        if s[i % l] != '1':
            print(s[i % l])
            break
        elif i == k - 1:
            print('1')
