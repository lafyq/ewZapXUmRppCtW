import poplib

M = poplib.POP3('pop.163.com')
M.user('yihe6383925@163.com')
M.pass_('k645393')
numMessages = len(M.list()[1])
print(numMessages)



# for i in range(numMessages):
#     for j in M.retr(i+1)[1]:
#         print(j)