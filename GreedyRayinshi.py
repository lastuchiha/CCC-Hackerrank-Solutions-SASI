n = int(input())
nums = list(map(int, input().split()))

sc1 = sc2 = 0
i = 0
while len(nums) > 0:
    if nums[0] < nums[-1]:
        res = nums.pop()
    else:
        res = nums.pop(0)
             
    if i%2:
        sc2 += res
    else:
        sc1 += res
    i += 1
    
print(sc1, sc2)
