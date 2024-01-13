print("Ahmed Nassar")

UserQuestion = ''

while(UserQuestion != 'n' or UserQuestion != 'N'):

    UserQuestion = input("do you want to enforce your password ? y/n : ")

    if(UserQuestion == 'y' or UserQuestion == 'Y'):

        UserPass = input("enter your password : ")

        counta = 0
        counts = 0
        countb = 0
        county = 0
        counte = 0
        countt = 0
        counto = 0
        counti = 0

        EnforcedPass = []

        for Letter in UserPass:
            EnforcedPass.append(Letter)

        for i in EnforcedPass:
            if(i.lower() == 'a'):
                counta += 1
            elif(i.lower() == 's'):
                counts += 1
            elif(i.lower() == 'b'):
                countb += 1
            elif(i.lower() == 'y'):
                county += 1
            elif(i.lower() == 'e'):
                counte += 1
            elif(i.lower() == 't'):
                countt += 1
            elif(i.lower() == 'o'):
                counto += 1
            elif(i.lower() == 'i'):
                counti += 1
            else:
                pass
            
            if(counta > 1):
                for ja in range(len(EnforcedPass)):
                    if(EnforcedPass[ja].lower()=='a'):
                        EnforcedPass[ja] = str(4)
                        
            if(counts > 1):
                for js in range(len(EnforcedPass)):
                    if(EnforcedPass[js].lower()=='s'):
                        EnforcedPass[js] = str(5)

            if(countb > 1):
                for jb in range(len(EnforcedPass)):
                    if(EnforcedPass[jb].lower()=='b'):
                        EnforcedPass[jb] = str(6)

            if(county > 1):
                for jy in range(len(EnforcedPass)):
                    if(EnforcedPass[jy].lower()=='y'):
                        EnforcedPass[jy] = str(9)
            
            if(counte > 1):
                for je in range(len(EnforcedPass)):
                    if(EnforcedPass[je].lower()=='e'):
                        EnforcedPass[je] = str(3)

            if(countt > 1):
                for jt in range(len(EnforcedPass)):
                    if(EnforcedPass[jt].lower()=='t'):
                        EnforcedPass[jt] = str(7)

            if(counto > 1):
                for jo in range(len(EnforcedPass)):
                    if(EnforcedPass[jo].lower()=='o'):
                        EnforcedPass[jo] = str(0)

            if(counti > 1):
                for ji in range(len(EnforcedPass)):
                    if(EnforcedPass[ji].lower()=='i'):
                        EnforcedPass[ji] = str(1)
            


        EnforcedPassStr = ""

        for C in EnforcedPass:
            EnforcedPassStr+=C

        print(f"your old password was : {UserPass}")

        print(f"your enforced password is : {EnforcedPassStr}")

    else:
        if(UserQuestion == 'n' or UserQuestion == 'N'):
            print("ok!")
            print("the program has EXIT!")
            break
