def find_short(s):
    s = list(s.split(" "))
    new_list = []
    for i in s:
        new_list.append(len(i))
    return min(new_list)
