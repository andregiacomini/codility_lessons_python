# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    zero_counter = int()
    max_zero_counter = int()
    count_gap = bool()
    for i in range(N.bit_length()):
        x = bin(1&N>>i)
        if x == bin(1):
            count_gap = True
        if count_gap:
            if x == bin(0):
                zero_counter += 1
            if x == bin(1):
                if zero_counter > max_zero_counter:
                    max_zero_counter = zero_counter
                zero_counter = 0
    
    return max_zero_counter

print(solution(4558935))