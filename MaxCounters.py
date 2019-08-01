
def solution(N:int(), A:[]):
    counters = [0] * N
    max_value = int()
    max_value_command = int()
    for i, val in enumerate(A):
        print(counters)
        if 1 <= val <= N:
            if counters[val-1] < max_value_command:
                counters[val-1] = max_value_command
            counters[val-1] += 1
            if counters[val-1] > max_value:
                max_value = counters[val-1]
        elif val == N + 1:
            max_value_command = max_value

    for i, val in enumerate(counters):
        if counters[i] < max_value_command:
            counters[i] = max_value_command
    return counters

print(solution(5,[3,4,4,6,1,4,4]))
print(solution(1, [2, 1, 1, 2, 1]))
