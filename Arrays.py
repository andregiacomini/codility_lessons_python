def solution(N:[]):
    if len(N)%2==0:
        return 0
    if len(N) > 1000000:
        return 0
    N.sort()
    print(N)
    for i in range(0, len(N), 2):  
        if i == len(N)-1:
            return N[i]
        if N[i] == N[i+1]:
            continue
        else:
            return N[i]

    


    
print(solution([1,2,1,4,6,5,4,5,1,2,1,2,2]))