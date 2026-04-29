def merge_sort(t):
    if len(t) <= 1:
        return t
    m = len(t) // 2
    l = merge_sort(t[:m])
    r = merge_sort(t[m:])
    return sorted(l + r)
 
print(merge_sort([5, 2, 9, 1]))
