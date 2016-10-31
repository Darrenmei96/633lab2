#Main File 

import user
import DAC
import RBAC

def main():
    
        



	
user = []
for i in range (1,6):
    user.append(User())
    user[i-1].loadfile(dataloc + "User" + str(i) + ".txt" )
    print ("User" + str(i) + " has been loaded into memory")

user[0].threshold = 80
user[1].threshold = 78
user[2].threshold = 75
user[3].threshold = 75
user[4].threshold = 78

#user = User()
#name = input("Enter in a username: ")

#calculate the deviations and false rejects for each user
deviations = []
falserejects = []
for i in range(0,5):
    tmp = []
    tmp2 = []
    for x in range (1,6):
        deviation = devs(user[i].fly[0:n],user[i].fly[x*n:x*n+n],user[i].dwell1[0:n],user[i].dwell1[x*n:x*n+n])
        tmp.append(deviation)
        tmp2.append(fr(deviation,user[i].threshold))
    deviations.append(tmp)
    falserejects.append(tmp2)

#calculate the false accept deviations
fadeviations = []
falseaccepts = []
for i in range(0, 5):
    tmp = []
    tmp2 = []
    for x in range (0,5):
        #if the same user, skip
        if x == i:
            continue
        tmp3 = []
        tmp4 = []
        for y in range (1,6):
            deviation = devs(user[i].fly[0:n],user[x].fly[y*n:y*n+n],user[i].dwell1[0:n],user[x].dwell1[y*n:y*n+n])
            tmp3.append(deviation)
            tmp4.append(fa(deviation,user[i].threshold))
        tmp.append(tmp3)
        tmp2.append(tmp4)
    fadeviations.append(tmp)
    falseaccepts.append(tmp2)

for i in range(0,5):
    print("User "+ str(i+1))
    print("Deviations: ", deviations[i])
    print("False Rejects: ", falserejects[i])
    print("False Reject Rate(Threshold",user[i].threshold, "): ", rate(falserejects[i])*100, "%")
    for j in range (0,4):
        usrno = j + 1
        if i == j:
            usrno += 1
        print("FA Deviations User "+str(usrno), ": ", fadeviations[i][j])
        print("False Accepts: ", falseaccepts[i][j])
        print("False Accept Rate(Threshold",user[i].threshold, "): ", rate(falseaccepts[i][j])*100, "%")
    print("")


if __name__ == "__main__":
    main()
