score = [0]*5

avg = 0
high =0

for i in range (0,5):
    print("성적을 입력해주세요")
    score[i] = input()
    avg+=int(score[i])

avg /= len(score)

score.sort()
high = score[len(score)-1]


print("평균은", avg)
print("최고점수는", high)
