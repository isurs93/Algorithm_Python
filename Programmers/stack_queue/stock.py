def solution(prices):
    answer = []
    pricesList = list(map(int, prices))
    pricesList.pop(0)
    
    for index in range(0, len(prices)-1):
        result = 1
        for data in pricesList:
            if data-prices[index] < 0 or result == len(pricesList):
                answer.append(result)
                pricesList.pop(0)
                break
            else:
                result += 1

    answer.append(0)
    return answer