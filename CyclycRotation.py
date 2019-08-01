def solution(N:[], K:int()):
    last_value = int()
    if len(N) != 0:
        for i in range(K):
            last_value = N.pop(len(N)-1)
            N.insert(0,last_value)

    return N

print(solution([], 3))