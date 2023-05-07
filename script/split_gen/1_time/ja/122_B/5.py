def main():
    s = input()
    max_len = 0
    cur_len = 0
    for c in s:
        if c in "ACGT":
            cur_len += 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)
    print(max_len)
