def main():
    s = input()
    max_length = 0
    length = 0
    for c in s:
        if c in 'ACGT':
            length += 1
            max_length = max(max_length, length)
        else:
            length = 0
    print(max_length)
