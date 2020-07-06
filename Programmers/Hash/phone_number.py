phone_book = ['119', '97674223', '1195524421']	
phone_book = ['123','456','789']
phone_book = ['1','123','1235','567','88']
answer = True    
prefix = phone_book[0]

for index in range(1, len(phone_book)):   
    testStr = ''
    if len(phone_book[index]) < len(prefix):
        answer = True
    else:
        for digits in (0, len(prefix)-1):
            testStr += phone_book[index][digits]

        if testStr == prefix:
            answer = False
            break

print(answer)