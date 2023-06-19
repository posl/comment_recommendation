def comma_count(n):
    if n < 1000:
        return 0
    else:
        return comma_count(n//1000) + 1

if __name__ == '__main__':
    comma_count()