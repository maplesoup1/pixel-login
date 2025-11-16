# Question B: CargoCraft Fleet
# Type A: 4 units, Type B: 6 units
# Min crafts: use more Type B, Max crafts: use more Type A

def solve(n):
    # Odd numbers or n=2 are impossible
    if n % 2 != 0 or n == 2:
        return -1, -1
    if n == 0:
        return 0, 0
    
    # Min crafts: maximize use of 6
    if n % 6 == 0:
        min_crafts = n // 6
    elif n % 6 == 2:
        min_crafts = (n - 8) // 6 + 2
    else:  # n % 6 == 4
        min_crafts = n // 6 + 1
    
    # Max crafts: maximize use of 4
    if n % 4 == 0:
        max_crafts = n // 4
    else:  # n % 4 == 2
        max_crafts = (n - 6) // 4 + 1
    
    return min_crafts, max_crafts

t = int(input())
for _ in range(t):
    n = int(input())
    result = solve(n)
    if result[0] == -1:
        print(-1)
    else:
        print(result[0], result[1])
