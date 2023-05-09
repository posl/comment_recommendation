def main():
    s = input()
    count = 0
    maxcount = 0
    for i in s:
        if i in 'ACGT':
            count += 1
        else:
            count = 0
        if count > maxcount:
            maxcount = count
    print(maxcount)
