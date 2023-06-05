def f(w):
    if w<=3:
        return [1,2,3][:w]
    elif w%2:
        return [1,2]+f(w-3)
    else:
        return [2,3]+f(w-5)
w=int(input())
l=f(w)
print(len(l))
print(*l)
