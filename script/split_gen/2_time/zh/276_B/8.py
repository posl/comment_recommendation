def main():
    s = input()
    a = s.rfind('a')
    print(a+1 if a != -1 else -1)
