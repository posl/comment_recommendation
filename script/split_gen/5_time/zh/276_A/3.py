def main():
    s = input()
    if s.count('a') == 0:
        print(-1)
    else:
        print(s.rfind('a') + 1)
