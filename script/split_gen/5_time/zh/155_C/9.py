def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 0
    max = 0
    for i in range(n):
        if i == 0:
            count = 1
            max = 1
        else:
            if s[i] == s[i-1]:
                count += 1
                if count > max:
                    max = count
            else:
                count = 1
    for i in range(n):
        if i == 0:
            count = 1
        else:
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
        if count == max:
            print(s[i])
