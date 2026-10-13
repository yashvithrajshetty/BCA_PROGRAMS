message='good morning'    #single line comment
my_string="hi how are you"   #single line string
my_para='''good morning
how are you '''            # multi-line string

#indexing
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[5])
print(message[6])
print(message[7])
print(message[8])
print(message[9])
print(message[10])
print(message[11]) 
print(message[-0])
print(message[-1])
print(message[-2])
print(message[-3])
print(message[-5])
print(message[-6])
print(message[-7])
print(message[-8])
print(message[-9])
print(message[-10])
print(message[-11]) 
  
print(message[0:3])
print(message[0:2])
#methods
print(message.lower())
print(message.upper())
print(message.strip())
print(message.__len__())
print(message.count(message))
print(message.split())
print(message.title())
print(message.replace('morning','night'))
