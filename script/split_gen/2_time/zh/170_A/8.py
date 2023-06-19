def main():
    x = input()
    x = x.split()
    for i in range(0, len(x)):
        if x[i] == '0':
            print(i+1)
            break
