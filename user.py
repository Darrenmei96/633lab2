n = 500
threshold = 0.7

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
print(user.deviation(1),user.deviation(2),user.deviation(3),user.deviation(4),user.deviation(5))
