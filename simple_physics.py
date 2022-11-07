#detailed user input for solving the equations
problem_selection=input("Please type the unknown variable name in block letters(Example:MAX HEIGHT):")


#Velocity
if problem_selection=="VELOCITY":
    print("Please type the formula number you want use as shown below")
    print("1.s=((u+v)/2)t")
    print("2.v**2=u**2+2gh")
    print("3.v**2=u**2+2as")
    print("4.v=u+at")
    print("5.v=u+gt")
    print("6.s=vt")
    print("7.E(kinetic)=1/2mv**2")
    formula=input("Type formula number:")
    if formula=="1":
        s=float(input("Enter displacement value(metre):"))
        u=float(input("Enter old velocity value(m/s):"))
        t=float(input("Enter time value(seconds):"))
        result=((2*s)/t)-u
        print(float(result),"m/s")
    if formula=="2":
        h=float(input("Enter height value(metre):"))
        u=float(input("Enter old velocity value(m/s):"))
        import math
        result=math.sqrt(u**2+2*9.8*h)
        print(float(result),"m/s")
    if formula=="3":
        s=float(input("Enter displacement value(metre):"))
        u=float(input("Enter old velocity value(m/s):"))
        a=float(input("Enter accelaration value(m/s**2):"))
        import math
        result=math.sqrt(u**2+2*a*s)
        print(float(result),"m/s")
    if formula=="4":
        u=float(input("Enter old velocity value(m/s):"))
        a=float(input("Enter accelaration value(m/s**2):"))
        t=float(input("Enter time value(seconds):"))
        result=u+a*t
        print(float(result),"m/s")
    if formula=="5":
        u=float(input("Enter old velocity value(m/s):"))
        t=float(input("Enter time value(seconds):"))
        result=u+9.8*t
        print(float(result),"m/s") 
    if formula=="6":
        s=float(input("Enter displacement value(metre):"))
        t=float(input("Enter time value(seconds):"))
        result=s/t
        print(float(result),"m/s")
    if formula=="7":
        E=float(input("Enter kinetic energy value(Joule):"))
        m=float(input("Enter mass value(kg):"))
        import math
        result=math.sqrt((2*E)/m)
        print(float(result),"m/s")
#displacement
if problem_selection=="DISPLACEMENT":
    print("Please type the formula number you want use as shown below")
    print("1.s=((u+v)/2)t")
    print("2.s=ut+1/2at**2")
    print("3.v**2=u**2+2as")
    print("4.s=vt")
    formula=input("Type formula number:")
    if formula=="1":
        u=float(input("Enter old velocity value(m/s):"))
        v=float(input("Enter new velocity value(m/s):"))
        t=float(input("Enter time value(seconds):"))
        result=((u+v)/2)*t
        print(float(result),"m")
    if formula=="2":
        u=float(input("Enter old velocity value(m/s):"))
        a=float(input("Enter accelaration value(m/s**2):"))
        t=float(input("Enter time value(seconds):"))
        result=u*t+(0.5*a*t**2)
        print(float(result),"m")
    if formula=="3":
        v=float(input("Enter new velocity value(m/s):"))
        u=float(input("Enter old velocity value(m/s):"))
        result=(v**2-u**2)/(2*a)
        print(float(result),"m")
    if formula=="4":
        v=float(input("Enter new velocity value(m/s):"))
        t=float(input("Enter time value(seconds):"))
        result=v*t
        print(float(result),"m")
#accelaration
if problem_selection=="ACCELARATION":
    print("Please type the formula number you want use as shown below")
    print("1.s=ut+1/2at**2")
    print("2.v**2=u**2+2as")
    print("3.v=u+at")
    formula=input("Type formula number:")
    if formula=="1":
        u=float(input("Enter old velocity value(m/s):"))
        s=float(input("Enter displacement value(metre):"))
        t=float(input("Enter time value(seconds):"))
        result=(2*(s-u*t))/t**2
        print(float(result),"m/s**2")
    if formula=="2":
        s=float(input("Enter displacement value(metre):"))
        u=float(input("Enter old velocity value(m/s):"))
        v=float(input("Enter new velocity value(m/s):"))
        result=(v**2-u**2)/(2*s)
        print(float(result),"m/s**2")
    if formula=="3 ":
        u=float(input("Enter old velocity value(m/s):"))
        v=float(input("Enter new velocity value(m/s):"))
        t=float(input("Enter time value(seconds):"))
        result=(v-u)/t
        print(float(result),"m/s**2")
#Max height
if problem_selection=="MAX HEIGHT":
    print("Formula:H=u**2/2g")
    u=float(input("Enter throwing velocity value(m/s):"))
    result=u**2/(2*9.8)
    print(float(result),"m")
#Efficiancy
if problem_selection=="EFFICIANCY":
    print("Formula:n=p/P*100% or n=w/W*100%")
    w_or_p=float(input("Enter net Energy or power value(Joule or Watt):"))
    W_or_P=float(input("Enter total Energy or power value(Joule or Watt):"))
    result=(w_or_p/W_or_P)*100
    print(float(result),"percent")
#power
if problem_selection=="POWER":
    print("Please type the formula number you want use as shown below")
    print("1.p=Fs/t")
    print("2.p=mgh/t")
    print("3.p=mas/t")
    print("4.p=w/t")
    formula=input("Select formula number:")
    if formula=="1":
        F=float(input("Enter force value(Newton):"))
        s=float(input("Enter displacement value(metre):"))
        t=float(input("Enter time value(seconds):"))
        result=(F*s)/t
        print(float(result),"Watt")
    if formula=="2":
        m=float(input("Enter mass value(kg):"))
        h=float(input("Enter height value(metre):"))
        t=float(input("Enter time value(seconds):"))
        result=(m*9.8*h)/t
        print(float(result),"Watt")
    if formula=="3":
        m=float(input("Enter mass value(kg):"))
        s=float(input("Enter displacement value(metre):"))
        a=float(input("Enter accelaration value(m/s**2):"))
        t=float(input("Enter time value(seconds):"))
        result=(m*a*s)/t
        print(float(result),"Watt")
    if formula=="4":
        w=float(input("Enter work value(Joule):"))
        t=float(input("Enter time value(seconds):"))
        result=w/t
        print(float(result),"Watt")
#buoyancy
if problem_selection=="BUOYANCY":
    print("Formula:P=Vpg")
    p=float(input("Enter specific density value(kgm**-3):"))
    V=float(input("Enter volume value(m**3):"))
    result=V*p*9.8
    print(float(result),"N")
#static energy
if problem_selection=="STATIC ENERGY":
    print("Formula:W=mgh")
    m=float(input("Enter mass value(kgm**-3):"))
    h=float(input("Enter height value(metre):"))
    result=m*9.8*h
    print(float(result),"J")
   

    
