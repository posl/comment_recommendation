def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    names.sort()
    max = 0
    max_name = ""
    for name in names:
        if names.count(name) > max:
            max = names.count(name)
            max_name = name
    print(max_name)
