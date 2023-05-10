def main():
    s = input()
    s = s.split('R')
    print(max([len(i) for i in s]))
