def main():
    a, b, d = map(int, input().split())
    #print(a, b, d)
    #print(math.cos(math.radians(d)))
    #print(math.sin(math.radians(d)))
    print(a * math.cos(math.radians(d)) - b * math.sin(math.radians(d)), a * math.sin(math.radians(d)) + b * math.cos(math.radians(d)))
