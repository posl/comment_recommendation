def countCommas(N):
    if N < 1000:
        return 0
    else:
        return N // 1000 + countCommas(N // 1000)

if __name__ == '__main__':
    countCommas()