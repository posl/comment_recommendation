def main():
    s = input()
    k = int(input())
    
    count = 0
    for c in s:
        if c == '1':
            count += 1
        else:
            break
    if k <= count:
        print(1)
    else:
        print(s[count])
