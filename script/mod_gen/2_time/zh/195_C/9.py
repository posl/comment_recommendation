def count_commas(n):
    if n < 1000:
        return 0
    else:
        return n//1000 + count_commas(n//1000)

if __name__ == '__main__':
    count_commas()