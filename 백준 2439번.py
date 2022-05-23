# n = int(input())

# for i in range(1,n+1):
#     print(" " * (n-i) + i * "*")

n = int(input())

for i in range(1,n+1):
     print(str(i * "*").rjust(n))

#오른쪽 정렬을 사용하여 클리어.
#위 주석은 다른사람의 문제풀이임.