def main():
    s = input()
    if s.find('a') == -1:
        print(-1)
    else:
        print(s.rfind('a') + 1)
