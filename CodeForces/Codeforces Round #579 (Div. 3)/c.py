def gcd( a, b ):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
ans = a[0]

for i in range(1, n):
    ans = gcd(ans, a[i])

print(ans)
