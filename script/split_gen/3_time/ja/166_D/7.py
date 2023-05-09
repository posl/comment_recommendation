def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(-118,119):
        for j in range(-119,118):
            if i**5 - j**5 == X:
                A = i
                B = j
                break
    print(A,B)
