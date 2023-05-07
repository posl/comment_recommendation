def main():
    str = input()
    for i in range(10):
        if str.find(str(i)) == -1:
            print(i)
            break
