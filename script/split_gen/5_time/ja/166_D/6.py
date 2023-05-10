def main():
    x = int(input())
    a = -1
    b = -1
    for i in range(-118,120):
        for j in range(-119,119):
            if i**5 - j**5 == x:
                a = i
                b = j
                break
        if a != -1:
            break
    print(a,b)
