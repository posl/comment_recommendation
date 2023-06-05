def main():
    n = int(input())
    files = []
    for i in range(n):
        files.append(input())
    for i in range(n):
        if files.count(files[i]) == 1:
            print(files[i])
        else:
            print(files[i] + "(" + str(files[0:i].count(files[i])) + ")")
