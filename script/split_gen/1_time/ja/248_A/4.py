def main():
    s = input()
    for i in range(10):
        if s.find(str(i)) == -1:
            print(i)
            break
