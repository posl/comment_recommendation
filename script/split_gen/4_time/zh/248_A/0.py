def main():
    s = input()
    s = list(s)
    for i in range(10):
        if str(i) not in s:
            print(i)
            break
