def main():
    s = input()
    t = input()
    counter = 0
    for i in range(3):
        if s[i] == t[i]:
            counter += 1
    print(counter)
