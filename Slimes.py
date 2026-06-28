x = int(input())
for i in range(x):
    n = int(input())
    a = list(map(int,input().split()))
    result = (max(a) - min(a) + 1) // 2
    print(result)
