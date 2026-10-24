def max_energy():
    arr = [-123] + [1] * 343 + [-123]
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current += x
        if current > best: best = current
    return best

print("The best energy sub array is: ", max_energy())