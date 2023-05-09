def main():
    X = int(input())
    for a in range(-120, 120):
        for b in range(-120, 120):
            if a**5 - b**5 == X:
                print(a, b)
                return
