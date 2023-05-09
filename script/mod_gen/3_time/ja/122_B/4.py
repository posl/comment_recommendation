def main():
    s = input()
    max_len = 0
    current_len = 0
    for c in s:
        if c in 'ACGT':
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 0
    max_len = max(max_len, current_len)
    print(max_len)

if __name__ == '__main__':
    main()