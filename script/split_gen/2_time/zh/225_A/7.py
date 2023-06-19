def main():
    s = input()
    s = sorted(s)
    #print(s)
    count = 0
    for i in range(3):
        for j in range(i+1, 3):
            if s[i] != s[j]:
                count += 1
    print(count+1)
