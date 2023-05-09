def main():
    s = input()
    k = int(input())
    s = s.replace('.', '')
    print(max(len(s) + min(k, len(s) - 1), len(s)))
