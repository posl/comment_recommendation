def f(x):
    return 1 if x == 0 else x * f(x-1)
h1, h2, h3, w1, w2, w3 = map(int, input().split())
print(f(h1+h2+h3)//f(h1)//f(h2)//f(h3)//f(w1)//f(w2)//f(w3))
