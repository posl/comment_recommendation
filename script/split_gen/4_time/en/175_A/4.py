def main():
    s = input()
    count = 0
    max = 0
    for i in s:
        if i == 'R':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
