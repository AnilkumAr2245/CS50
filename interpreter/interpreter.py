expression=input("Expression:")
x,y,z=expression.split()
x=float(x)
z=float(z)
if (y =="+"):
    ans=(x+z)
    print(f"{ans:.1f}")
elif (y == "-"):
    ans=(x-z)
    print(f"{ans:.1f}")
elif (y == "*"):
    ans=(x*z)
    print(f"{ans:.1f}")
elif(y == "/"):
    ans=(x/z)
    print(f"{ans:.1f}")

