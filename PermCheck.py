def solution(N:[]):
    if len(N) > 100000:
        return 0
    N.sort()
    last_value = int()
    for i, val in enumerate(N):
        if val < 1:
            return 0
        if val > 1000000000:
            return 0
        if i == 0:
            if val != 1:
                return 0
            last_value = val
        else:
            if val - last_value != 1:
                return 0
            last_value = val
    return 1

assert solution([4,1,3,2]) == 1
assert solution([4,1,3]) == 0
assert solution([4,2]) == 0
assert solution([4,3]) == 0
assert solution([2,1]) == 1
