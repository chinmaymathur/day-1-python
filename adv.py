# a = [1,2,3,4] 
# name = "hello "
# tpl = (     )
# lst  = [    ]
# dct  = {key and value }
# set = {      } 


# print(a)

# print(a[0])
# print(a[3])

# # slicing
# print(a[-1])
# apend
# a.append(8)
# print(a)

# a.insert(2,55)
# print(a)
# a.pop() # remove the last element
# print(a)
# a.insert(2,8)
# print(a)
# print(a)
# b = [55,44,22,1,3,9]
# print(b)
# b.sort()
# print(b)
# for x in b:
# print(x)

# for y in range(1,10):
# print(y)

#for y in range (1,10):
# print(y)


# >>>>>>>>>>>>>Dict<<<<<<<<<<
#dct = {'name':'Rohit','cls':"second year",'roll no.':"21eaycs055"}
#print(dct)
# print(dct['name'])
# del dct['cls']
# print(dct)
# dct.pop('roll no.')
# print(dct)
# check_key='name' in dct
# print(check_key)
# dct.clear()
# print(len(dct))

#>>>>>>>>>>>>>> update <<<<<<<<<
#print(dct.keys())
#print(dct.values())
# lst.append()
# print(list)

# >>>>>>>>>>>>>set<<<<<<<<<<<
# s = { 20,55,'hello'}
# s[0]


# if 
# elif
# else


#>>>>>>>>>>>>>>>#operator


x =  (1,2,3,4)
y = (5,6,4,7)
print(x+y)


num1 = 8
num2 = 4
addition = num1 + num2
print(f"{num1} + {num2} = {addition}")

subtraction = num1 - num2
print(f"{num1} - {num2} = {subtraction}")


multiplication = num1 * num2
print(f"{num1} * {num2} = {multiplication}")


division = num1 / num2
print(f"{num1} / {num2} = {division}")

modulus = num1 % num2
print(f"{num1} % {num2} = {modulus}")

#comparison operator
#equal to 
a = 5
b = 5
result = (a==b)
print(result)
# not equal to 
a = 5
b = 5
result = (a!=b)
print(result)

a = 5
b = 5
result = (a>b)
print(result)

#greater than equal to 
a = 5
b = 5
result = (a<=b)
print(result)

#assigment opearator 
a = 5
a+= 3
print(a)


a = 5
a-= 3
print(a)


a = 5
a/= 3
print(a)

a = 5
a**= 3
print(a)


a = 5
a//= 3
print(a)



a = True
b = False
result = a and b  # result is False
print(result)


a = True
b = False
result = a or b  # result is True


a= 7
b=4
if a==b:

    print("right ")
    pass
elif a>b:
    print("hello guys")

else:
    print("wrong")
    pass


# update in dictionari
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  


a = 0
while a<5:
    print(a)
    a+=1
    i=1

    
#while
sum = 0
num = 1
while num<=100:
    sum+=num
    num+=1
    print("sum of number from 1 to 100",[sum])


def add(x,y):
 print(x+y)
 add(5,8)
                                                    #day2
# string data type

st = """upflair pvt ltd
3021251h """
print(st)
print(type(st))

#indexing print[star:end:jump]
st = 'upflairs'
print(st)
print(st[-7])
print(st[-3])
print(st[::5])

st = 'upflair'
print(st.capitalize()) #FUNCTIONS capital
print(st.title())
print(len(st))
print(st.split(','))
print(st.replace(',',' ' ))
print(st.replace('upflair','flipkart'))
print(st.replace('p','f'))
print(st.endswith('n'))
# list

ls = [1,2.9,3,4,56,]
print(ls)
print(type(ls))
print(ls[2: ])
ls.append[1]('hello')
print(ls)
ls.pop(2)
print(ls)
ls.append('hello')
print(ls)


ls =[10,20,30,40,50,60,True,[85,41,52,63,'upflair'],25]
print(ls)

#set -> no duplicate value allowed  , not  maintain order
st = { 25,65,3,4,6,6,3,56,4}
print(st) 




























