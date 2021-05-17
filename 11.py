# print( "Hello world 0" )
# print( "Hello world 3" )
# print( "Hello world 6" )
# print( "Hello world 9" )
# print( "Hello world 12" )
# print( "Hello world 15" )
# print( "Hello world 18" )
# print( "Hello world 21" )
# print( "Hello world 24" )
# print( "Hello world 27" )

while False :
    print('Hello world')
print('After while')

i = 0
while i < 3:
    print('Hello world')
    i = i + 1
while i < 10:
    print('Hello world' + str(i*3)+'")')
    i = i + 1
while i < 10:
    if i == 4:
        print(i)
    i = i + 1

i = 0
while i < 10:
    if i == 4:
        break
    print(i)
    i = i + 1
print("after while")    
