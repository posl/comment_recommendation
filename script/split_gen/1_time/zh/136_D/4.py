def main():
    s = input()
    n = len(s)
    result = [0] * n
    for i in range(n):
        if s[i] == 'R' and s[i+1] == 'L':
            result[i] += 1
            result[i+1] += 1
            i += 2
        elif s[i] == 'R':
            result[i] += 1
            i += 1
        elif s[i] == 'L' and s[i-1] == 'R':
            result[i-1] += 1
            result[i] += 1
            i += 2
        elif s[i] == 'L':
            result[i] += 1
            i += 1
    print(result)
