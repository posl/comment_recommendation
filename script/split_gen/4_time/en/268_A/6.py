def main():
    a = input()
    a = a.split(' ')
    a = [int(i) for i in a]
    print(len(set(a)))
