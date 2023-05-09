def main():
    s = input()
    s = set(s)
    for i in range(10):
        if str(i) not in s:
            print(i)
            return
