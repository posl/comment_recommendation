def main():
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        if str(i).find('7') >= 0:
            continue
        if str(oct(i)).find('7') >= 0:
            continue
        result += 1
    print(result)
main()
