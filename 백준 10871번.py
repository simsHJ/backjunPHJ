n , x =map(int, input().split())
output = []
p = input().split(" ")

for i in p:
    if int(i) < x :
        output.append(i)
print(" ".join(output))

#형의 도움으로 풀었음. 다시한번더 볼것