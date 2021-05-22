# alphabet = "abcdefghijklmnopqrstuvwxyz"
# word_list = []
# word_num = []
#
# word = str(input())
# for i in word:
#     word_list.append(i)
#
# for character in alphabet:
#     for i in range(len(word_list)):
#         if character == word_list[i]:
#             word_num.append(i)
#             break
#         elif i < len(word_list)-1: continue
#         else:
#             word_num.append(-1)
# for i in word_num:
#     print(i,end=" ")

S = input()

alp = [-1] * 26

for i in range(len(S)):
    if alp[ord(S[i]) - 97]==-1:#-1이면 등장하지 않은 거니까
        alp[ord(S[i]) - 97]=i#써도 돼

for x in alp:
    print(x,end=' ')