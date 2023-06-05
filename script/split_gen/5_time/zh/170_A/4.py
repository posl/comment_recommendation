def main():
    str = input()
    str = str.split()
    for i in range(0, len(str)):
        if str[i] == '0':
            print(i+1)
            break
