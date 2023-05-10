def main():
    S = input()
    S = S[::-1]
    S = int(S)
    count = 0
    while True:
        if S == 0:
            break
        if S % 10 == 0:
            S = S // 10
            count += 1
        else:
            count += S % 10
            S = S - S % 10
    print(count)
