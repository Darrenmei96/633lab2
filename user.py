n = 500
dataloc = "Lab2-Sample-Files\\"

class User:
    def __init__(self):
        self.key1 = []
        self.key2 = []
        self.fly = []
        self.dwell1 = []
        self.dwell2 = []

    def loadfile(self,filename):
        #read all the lines
        #note that the first line[0] includes the header
        with open(filename, "r") as lines:
            for line in lines:
                array = line.split()
                try:
                    self.key1.append(int(array[0]))
                    self.key2.append(int(array[1]))
                    self.fly.append(int(array[2]))
                    self.dwell1.append(int(array[3]))
                    self.dwell2.append(int(array[4]))
                except ValueError:
                    pass
        lines.close()

    def deviation(self,userno):
        #dg,n1 = self.digraphs(userno)
        dg,n1 = sigmas(self.fly[0:n],self.fly[userno*n:userno*n+n])
        #mg,n2 = self.monographs(userno)
        mg,n2 = sigmas(self.dwell1[0:n],self.dwell1[userno*n:userno*n+n])
        d = (dg/(n1-1) + (mg/n2))*50
        return d

def fr(dev,threshold):
    return 1 if dev >= threshold else 0

def fa(dev,threshold):
    return 1 if dev <= threshold else 0

def sigmas(trefs, tmons):
        answer, count = 0.0, 0
        for i in range(0,len(trefs)):
            try:
                answer += abs(trefs[i]-tmons[i])/float(tmons[i])
                count += 1
            except ZeroDivisionError:
                pass
        return answer, count

user = []
for i in range (1,6):
    user.append(User())
    user[i-1].loadfile(dataloc + "User" + str(i) + ".txt" )
    print ("User" + str(i) + " has been loaded into memory")


#user = User()
#name = input("Enter in a username: ")

#calculate the deviations and false rejects for each user
deviations = []
falserejects = []
for i in range(0,5):
    tmp = []
    tmp2 = []
    for x in range (1,6):
        tmp.append(user[i].deviation(x))
        tmp2.append(fr(tmp[x-1],70))
    deviations.append(tmp)
    falserejects.append(tmp2)

for i in range(0,5):
    print("User "+ str(i+1))
    print("Deviations: ", deviations[i])
    print("False Rejects: ",falserejects)
    print("")

#calculate the false accept deviations
fadeviations = []
for i in range(0, 5):
    
