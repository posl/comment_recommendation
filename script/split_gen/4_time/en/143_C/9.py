def main():
    num = int(input())
    colors = input()
    prev = colors[0]
    count = 1
    for i in range(1, num):
        if prev != colors[i]:
            count += 1
            prev = colors[i]
    print(count)
