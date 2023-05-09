def solve(baggage, box, query):
    box.sort()
    for i in range(len(query)):
        l, r = query[i]
        temp = box[:l-1] + box[r:]
        temp.sort()
        box_size = [x[0] for x in temp]
        box_value = [x[1] for x in temp]
        #print(box_size, box_value)
        res = 0
        for j in range(len(baggage)):
            for k in range(len(box_size)):
                if baggage[j][0] <= box_size[k]:
                    res += box_value[k]
                    box_size.pop(k)
                    box_value.pop(k)
                    break
        print(res)
    return

if __name__ == '__main__':
    solve()