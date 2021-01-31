def solve():
    from itertools import product

    ans = 0
    for bit in product((0, 1), repeat=K):
        cnt = [0] * (N + 1) 
        for i in range(K):
            ball = people[i][bit[i]]
            cnt[ball] += 1

        score = 0
        for i in range(M):
            c, d = conditions[i]
            if cnt[c] > 0 and cnt[d] > 0:
                score += 1
        ans = max(ans, score)
    return ans


N, M = map(int, input().split())

conditions = []
for _ in range(M):
    a, b = map(int, input().split())
    conditions.append((a, b))

people = []
K = int(input())
for _ in range(K):
    c, d = map(int, input().split())
    people.append((c, d))

print(solve())
