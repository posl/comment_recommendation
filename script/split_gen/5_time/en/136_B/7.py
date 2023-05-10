def main():
    n = int(input())
    if n < 10:
        print(n)
        return
    result = 9
    if n < 100:
        print(result)
        return
    if n < 1000:
        result += n - 99
        print(result)
        return
    if n < 10000:
        result += 900
        result += n - 999
        print(result)
        return
    if n < 100000:
        result += 900
        result += 90000
        result += n - 9999
        print(result)
        return
    print(90909)
    return
