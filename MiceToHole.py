n = int(input())
mice = list(map(int, input().split()))
holes = list(map(int, input().split()))

time = []

mice.sort()
holes.sort()

for i in range(n):
    time.append(abs(mice[i] - holes[i]))
    
print(max(time))
