def main():
    k = int(input())
    n = 0
    while k > 0:
        n += 1
        if str(n).find('2') != -1:
            k -= 1
    print(n)
