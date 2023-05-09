def main():
    s = input()
    if s.rfind("a") == -1:
        print(-1)
    else:
        print(s.rfind("a")+1)
