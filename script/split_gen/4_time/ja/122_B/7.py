def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i in ['A', 'C', 'G', 'T']:
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        max = count
    print(max)
