def main():
    s = input()
    t = input()
    minChange = 1000
    for i in range(len(s)-len(t)+1):
        change = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                change += 1
        if minChange > change:
            minChange = change
    print(minChange)
