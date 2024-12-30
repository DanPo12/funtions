number=int(input("chose a number?"))
secondnumber=int(input("chose a seconde number?"))
operator=str(input("chose a operator +,-,*,/"))

if operator=="+":
    print(number+secondnumber)
elif operator=="-":
    print(number-secondnumber)
elif operator=="*":
    print(number*secondnumber)
elif operator=="/":
    print(number/secondnumber)
else :
    print("invalide operator!")