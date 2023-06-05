def problem168_b():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[:k] + "...")
    else:
        print(s)

if __name__ == '__main__':
    problem168_b()