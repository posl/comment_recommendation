def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 1
    count = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
            if count > max:
                max = coun
