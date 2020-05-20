import random

def alg1() :
	Max = [0] * (n)
	for i in range(0, n) :
		for j in range(0, i + 1) :
			if (Max[i] < A[j]) :
				Max[i] = A[j]
	return Max

def alg2() :
	Max = [0] * n
	Max[0] = A[0]
	for i in range(0, n - 1) :
		Max[i + 1] = max([Max[i], A[i + 1]])
	return Max

n = input("리스트 A의 원소의 개수를 입력하세요: ")
n = int(n)
A = list()

for i in range(0, n) :
    A.append(random.randrange(1, 100))

print("리스트 A의 원소:", A)
print("alg1으로 구한 최댓값 리스트: ", alg1())
print("alg2으로 구한 최댓값 리스트: ", alg2())
