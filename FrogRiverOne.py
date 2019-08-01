def solution(X:int(), A:[]):
    sum_terms_A = (X*(1+X))/2
    actual_sum_terms_A = int()
    got_element = [0]*X
    for i, val in enumerate(A):
        if got_element[val-1] == 0:
            got_element[val-1] = 1
            actual_sum_terms_A += val
            if actual_sum_terms_A == sum_terms_A:
                return i
    
    return -1


#print(solution(5, [1,3,1,4,2,3,5,4]))
print(solution(1, [1]))