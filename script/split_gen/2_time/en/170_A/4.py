def main():
    x = map(int, raw_input().split())
    for i in range(0, len(x)):
        if x[i] == 0:
            print i + 1
            break
main()
