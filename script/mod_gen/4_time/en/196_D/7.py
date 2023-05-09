def get_ways(h, w, a, b):
    # print(h, w, a, b)
    if h == 1 and w == 1:
        return 1
    if h == 1:
        return get_ways(h, w - 1, a, b - 1)
    if w == 1:
        return get_ways(h - 1, w, a - 1, b)
    if a == 0:
        return get_ways(h - 1, w, a, b - 1)
    if b == 0:
        return get_ways(h, w - 1, a - 1, b)
    return get_ways(h - 1, w, a, b - 1) + get_ways(h, w - 1, a - 1, b)
H, W, A, B = map(int, input().split())
print(get_ways(H, W, A, B))
I got TLE on this. I think I need to use memoization. I am not sure how to do that. Can you help?
Thanks
You can use a dictionary to memoize your function.
@harryharry
Thanks for your reply. I am not sure how to do that. Can you help?
Thanks
You can use a dictionary to memoize your function.
@harryharry
Thanks for your reply. I am not sure how to do that. Can you help?
Thanks
You can use a dictionary to memoize your function.
@harryharry
Thanks for your reply. I am not sure how to do that. Can you help?
Thanks
You can use a dictionary to memoize your function.
@harryharry
Thanks for your reply. I am not sure how to do that. Can you help?
Thanks
You can use a dictionary to memoize your function.
@harryharry
Thanks for your reply. I am not sure how to do that. Can you help?
Thanks
You can use a dictionary to memoize your function.
@harryharry
Thanks for your reply. I am not sure how to do that. Can you help?
Thanks
You can use a dictionary to memoize your function.
@harryharry
Thanks for your reply. I am not sure how to do that. Can you help?
Thanks
You can use

if __name__ == '__main__':
    get_ways()