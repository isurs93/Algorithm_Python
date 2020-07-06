# participant = ['mislav', 'stanko', 'mislav', 'ana']
# completion = ['stanko', 'ana', 'mislav']

# print(participant in completion)

participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']

# print(completion.count('vinko'))
####################################################################
# 1번 
####################################################################

answer = ''     
for index in participant:
    if participant.count(index) != completion.count(index):
        answer = index            
        break

# print(answer)
####################################################################
# 2번 
####################################################################
# answer = ''  
# result = False
# for index in range(0, len(participant), 2):
#         test = participant[index]
#         print(test)
#         if participant.count(test) != completion.count(test):
#             answer = test
#             result = True
#             break

# if result == False:
#     for index in range(1, len(participant), 2):
#         test = participant[index]
#         print(test)
#         if participant.count(test) != completion.count(test):
#             answer = test
#             break
# print(answer)

####################################################################
# 3번 
####################################################################
# def calc(participant, completion, startNum):
#     result = ''
#     for index in range(startNum, len(participant), 2):
#         test = participant[index]
#         if participant.count(test) != completion.count(test):
#             result = test
#             break
#     return result

# answer = ''   
# answer = calc(participant, completion, 0)
# if answer == '':
#     answer = calc(participant, completion, 1)

# print(answer)


####################################################################


