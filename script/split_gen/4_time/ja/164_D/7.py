def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(0,n):
        for j in range(i,n):
            if int(s[i:j+1])%2019 == 0:
                count += 1
    print(count)