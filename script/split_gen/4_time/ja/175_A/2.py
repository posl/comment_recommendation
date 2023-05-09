def main():
    s = input()
    max = 0
    count = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
