def main():
    s = input()
    result = 'Yes'
    for i in range(len(s)):
        if (i % 2 == 0 and s[i] == 'L') or (i % 2 == 1 and s[i] == 'R'):
            result = 'No'
            break
    print(result)
