def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_mod = [i%200 for i in a]
    #print(a_mod)
    a_mod_count = [0]*200
    for i in a_mod:
        a_mod_count[i] += 1
    #print(a_mod_count)
    ans = "No"
    for i in range(200):
        if a_mod_count[i] > 1:
            ans = "Yes"
            break
    if ans == "No":
        print(ans)
        return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
