def mid_max(n):
    arr = [-1,n,-1]
    best = arr[0]
    current = arr[0]
    for x in arr [1:]:
        if current < 0: current = x
        else: current = current+x
        if current>best : best = current
    return best
print("Mid max(3) = ", mid_max(3))
print("Mid_max(5) = ",mid_max(5))

o = int(input("Enter a number : "))
print(mid_max(o))