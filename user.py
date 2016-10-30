n = 500
<<<<<<< HEAD
threshold = 0.7
=======
dataloc = "Lab2-Sample-Files\\"
>>>>>>> 22b653b9038947f095efa3634f7fb1e0170c285e

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

<<<<<<< HEAD
    # Calculate the digraphs sum (fly time)
    #sum(|tref-tmon|/tmon)
    def digraphs(self,userno):
        j = userno * n
        answer,count = 0,0
        for i in range(0,n):
            try:
                answer += abs(self.fly[i]-self.fly[j+i])/self.fly[j+i]
                count += 1
            except ZeroDivisionError:
                pass
        return answer,count

    # Calculate the monographs sum (dwell time)
    #sum(|tref-tmon|/tmon)
    def monographs(self,userno):
        j = userno * n
        answer,count = 0,0
        for i in range(0,n):
            try:
                answer += abs(self.dwell1[i]-self.dwell1[j+i])/self.dwell1[j+i]
                count += 1
            except ZeroDivisionError:
                pass
        return answer,count

    def deviation(self,userno):
        dg,n1 = self.digraphs(userno)
        mg,n2 = self.monographs(userno)
        d = (dg/(n1-1) + (mg/n2))*50
        return d

    def fr(self,userno):
        return self.deviation(userno) >= threshold

    def fa(self,userno):
        return self.deviation(userno) <= threshold

user = User()
name = input("Enter in a username: ")
filename = "Lab2-Sample-Files\\"+name+".txt"
user.loadfile(filename)
#print(user.fly)
#print(user.fly.index(0))
print(user.deviation(1),user.deviation(2),user.devia
































































































































































































































      tion(3),user.deviation(4),user.deviation(5))
=======
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
    
>>>>>>> 22b653b9038947f095efa3634f7fb1e0170c285e
