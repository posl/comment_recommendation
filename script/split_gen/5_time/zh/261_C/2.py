def main():
    n = int(input())
    files = {}
    for _ in range(n):
        s = input()
        if s in files:
            files[s] += 1
            print(s + '(' + str(files[s]) + ')')
        else:
            files[s] = 0
            print(s)
