def main():
    n = int(input())
    s = input()
    print(s.replace(',', '.') if s.count('"') % 2 == 0 else s)
