def main():
    n = int(input())
    s = input()
    count = 1
    for i in range(1,n):
        if s[i-1] != s[i]:
            count += 1
    print(count)
