def main():
    s = input()
    count = 0
    maxcount = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count >= maxcount:
                maxcount = count
        else:
            count = 0
    print(maxcount)
