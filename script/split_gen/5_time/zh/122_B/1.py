def main():
    S = input()
    max_len = 0
    count = 0
    for s in S:
        if s in 'ACGT':
            count += 1
            if count > max_len:
                max_len = count
        else:
            count = 0
    print(max_len)
