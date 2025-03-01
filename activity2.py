height=int(input("Enter your Height"))
weight=int(input("Enter your Weight"))

bmi=weight/(height/100)**2

if bmi<18:
    print("You are under weight")
elif bmi<24:
    print("You are Healthy")
elif bmi<29:
    print("You are over Weight")
elif bmi<34:
    print("You are seaverly over weight")
elif bmi<39:
    print("You are obese")
else :
    print("ou are seaverly obese")

