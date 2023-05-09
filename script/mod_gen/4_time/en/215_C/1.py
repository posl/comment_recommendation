def permutation(string):
    if len(string) == 1:
        return [string]
    else:
        perm_list = []
        for a in string:
            remaining_elements = [x for x in string if x != a]
            z = permutation(remaining_elements)
            for t in z:
                perm_list.append([a] + t)
        return perm_list
#
#def permutation(string):
#    if len(string) == 1:
#        return [string]
#    else:
#        perm_list = []
#        for a in string:
#            remaining_elements = [x for x in string if x != a]
#            z = permutation(remaining_elements)
#            for t in z:
#                perm_list.append([a] + t)
#        return perm_list

if __name__ == '__main__':
    permutation()