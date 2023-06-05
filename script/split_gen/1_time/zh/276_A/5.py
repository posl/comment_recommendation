def main():
    s = input()
    s = s[::-1]
    if s.find('a') == -1:
        print(-1)
    else:
        print(len(s) - s.find('a'))
