n , k = [int(x) for x in input().split(" ")]
pos = [int(x) for x in input().split(" ")]

res = 0
window = 0
left = 0

for right in range(len(pos)):
        # Use sliding window and 2 pointers logic to solve
        while pos[right] - pos[left] >= k:
            if left < right : left += 1
        # Update the maximum rescued chicken
        window = right - left  +1
        if window > res : res = window
    
print("output : " ,res)

#test case from problem

# 5 5
# 2 5 10 12 15    #output 2

# 6 10
# 1 11 30 34 35 37    #output 4



#additional test cases including edge cases

# 9 10
# 1 7 11 30 34 35 37 39 40  #output 5

# 7 5
# 2 5 10 12 15 16 19 #output 3

# 1 10
# 12    #output 1



