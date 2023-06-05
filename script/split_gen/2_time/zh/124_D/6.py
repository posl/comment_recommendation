def main():
    n = int(input())
    s = input()
    if n == 1:
        print(0)
    else:
        print(min(s.count('0'),s.count('1'))*2)
