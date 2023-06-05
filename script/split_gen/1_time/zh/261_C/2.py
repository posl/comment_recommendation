def main():
    n = int(input())
    files = {}
    for i in range(n):
        file = input()
        if file in files:
            files[file] += 1
            print(file + "(" + str(files[file]) + ")")
        else:
            files[file] = 0
            print(file)
