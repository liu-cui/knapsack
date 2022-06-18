def dp(w, v, C):
    assert (len(w) == len(v) and C >= 0)
    n = len(w)
    taken = [0] * n
    if n == 0 or C == 0:
        return 0
    memo = [-1 for _ in range(C + 1)]
    for j in range(0, C + 1):
        memo[j] = v[0] if j >= w[0] else 0
    for i in range(1, n):
        for j in range(C, w[i] - 1, -1):
            memo[j] = max(memo[j], v[i] + memo[j - w[i]])
            if memo[j] != memo[j-1]:
                taken[i] = 1
    return memo[C], taken

