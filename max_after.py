def max_after(n):
    arr = [-n] + [1] * n
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current += x
        if current > best: best = current
    return best

input("max_after(n) finds the max subarray sum in [-n, 1, 1,1 ..... , 1]. Press enter ")
print(" max_after(3) =", max_after(3))

n = int(input("Enter n: "))
guess = input(f"What is max_after({str(n)}) ? ")
print(f"max_after({str(n)}) = {max_after(n)}, your guess = {guess}")
