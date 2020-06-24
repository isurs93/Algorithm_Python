count, target = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
nearResult = 0

for index1 in range(0, count-2):
    for index2 in range(index1+1, count-1):
        for index3 in range(index2+1, count):
            testResult = cards[index1] + cards[index2] + cards[index3]

            if testResult == target:
                result = testResult
                break
            elif target > testResult and testResult > nearResult:
                nearResult = testResult

if result == target:
    print(result)
else:
    print(nearResult)