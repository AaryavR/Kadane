def max_mid(n):
    arr = [-1, n, -1]
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current += x
        if current > best: best = current
    return best

input("max_mid(n) finds the max subarray sum in [-1, n, -1]. Press enter ")
print(" max_mid(3) =", max_mid(3))

n = int(input("Enter n: "))
guess = input(f"What is max_mid({str(n)}) ? ")
print(f"max_mid({str(n)}) = {max_mid(n)}, your guess = {guess}")
