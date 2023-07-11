def main():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    strings.sort()
    max_count = 0
    count = 0
    for i in range(n):
        if i == 0:
            count = 1
        else:
            if strings[i] == strings
