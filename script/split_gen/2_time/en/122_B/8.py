def main():
    S = input()
    max = 0
    count = 0
    for c in S:
        if c in ('A', 'C', 'G', 'T'):
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
