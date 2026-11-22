

n = int(input())

a = n // 10 
b = n % 10
if a // b == 0 or a % b == 0 :
    print("YES")

else :
    print("NO")