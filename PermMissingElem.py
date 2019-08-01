
def solution(N:[]):
    if len(N) == 0:
        return 1
    
    N.sort()
    if N[0] != 1:
        return 1
    if N[len(N)-1] != len(N)+1:
        return len(N)+1
    for i in N: 
        if N[i]-1 - i == 1:
            return N[i] - 1

print(solution([2,3,1,6]))