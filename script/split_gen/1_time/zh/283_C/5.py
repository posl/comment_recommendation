def main():
    S = input()
    S = int(S)
    count = 0
    while S > 0:
        if S % 10 == 0:
            S //= 10
            count += 1
        else:
            S -= 1
            count += 1
    print(count)
