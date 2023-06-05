def main():
    s = input()
    k = int(input())
    s = list(s)
    for i in range(k):
        if s[i] == '1':
            continue
        else:
            print(s[i])
            break
