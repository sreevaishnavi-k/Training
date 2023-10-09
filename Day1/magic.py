def magicPrime():
        num=int(input("enter a number"))
        rev=0
        rem=0
        c_flag=0
        r_flag=0
        while num>0:
            rem=num%10
            rev=rev+rem*10
            num=num//10
        for i in range(2,num):
            if num%i==0:
                c_flag+=1
        for i in range(2,rev):
            if rev%i==0:
                r_flag+=1
        if c_flag==0 and r_flag==0:
            print("magical prime number")
        else:
            print("not magical prime")
magicPrime()
