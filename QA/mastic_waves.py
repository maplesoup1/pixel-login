# Question A: Mystic Waves
# If n is odd, result is x; if n is even, result is 0

def solve(x, n):
    return x if n % 2 == 1 else 0

t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    print(solve(x, n))