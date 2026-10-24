def max_front(n):
    arr = [1]*n + [-1]
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current += x
        if current > best: best = current
    return best

input("max_front(n) finds the max subarray sum in [1, 1, 1, 1 ..... -1]. Press enter ")
print(" max_front(3) =", max_front(3))

n = int(input("Enter n: "))
guess = input(f"What is max_front({str(n)}) ? ")
print(f"max_front({str(n)}) = {max_front(n)}, your guess = {guess}")
