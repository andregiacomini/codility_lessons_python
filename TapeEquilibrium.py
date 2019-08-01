import sys

def solution(N:[]):
    lower = N[0]
    upper = sum(N) - lower
    min_dif = sys.maxsize
    current_dif = int()
    for i in range(len(N)-1):
        current_dif = abs(lower - upper)
        if abs(lower - upper) < min_dif:
            min_dif = current_dif
        lower += N[i+1]
        upper -= N[i+1]


    return min_dif

print(solution([2000,4000]))
