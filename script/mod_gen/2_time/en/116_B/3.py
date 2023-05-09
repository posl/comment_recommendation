def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if len(a) != len(set(a)):
        print(len(a))
        break
I'm not sure if this is the best way to do it, but I think it's pretty neat. I use the set function to get rid of all duplicates, and then compare the length of the list to the length of the set. If they are not the same, that means there are duplicates, and I can print the length of the list.
You can use the set function to get rid of all duplicates, and then compare the length of the list to the length of the set. If they are not the same, that means there are duplicates, and you can print the length of the list.
I'm not sure if this is the best way to do it, but I think it's pretty neat.
I think this is a pretty neat solution. I like how you used the set function to get rid of all duplicates and then compared the length of the list to the length of the set. If they are not the same, that means there are duplicates, and you can print the length of the list.
I'm not sure if this is the best way to do it, but I think it's pretty neat.
I think this is a pretty neat solution. I like how you used the set function to get rid of all duplicates and then compared the length of the list to the length of the set. If they are not the same, that means there are duplicates, and you can print the length of the list.
I'm not sure if this is the best way to do it, but I think it's pretty neat.
I think this is a pretty neat solution. I like how you used the set function to get rid of all duplicates and then compared the length of the list to the length of the set. If they are not the same, that means there are duplicates, and you can print the length of the list.
I'm not sure if this is the best way to do it, but I think it's pretty neat.
I think this is a pretty neat solution. I like how you used the set function to get rid of all duplicates and then compared the length of the list to the length

if __name__ == '__main__':
    f()