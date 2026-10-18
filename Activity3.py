def max_front(n):
    arr = [-n] + [1]*n
    best = arr[0]
    current = arr[0]
    for x in arr[1:]:
        if current<0: current = x
        else: current = current+x
        if current> best : best = current
    return best
print("max_front(5) = ",max_front(5))
print("max_front(6) = ",max_front(6))
p = int(input("Enter a number : "))
print(max_front(p))