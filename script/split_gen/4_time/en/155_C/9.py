def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 1
    max_count = 0
    max_string = ''
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_string = s[i]
            count = 1
    if count > max_count:
        max_string = s[n-1]
    print(max_string)
