def main():
    s = input()
    for i in range(10):
        if s.count(str(i)) == 0:
            print(i)
