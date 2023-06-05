def main():
    n = int(input())
    s = input()
    s = s.replace(',"', '.')
    s = s.replace('"', '')
    print(s)
