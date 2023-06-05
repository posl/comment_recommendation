def main():
    str = input()
    str_split = str.split()
    for i in range(0, 5):
        if str_split[i] == '0':
            print(i+1)
