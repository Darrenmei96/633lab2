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
        answer = 0
        for i in range(1,n):
            answer += abs(self.fly[i]-self.fly[j+i])/self.fly[j+i]
        return answer

    # Calculate the monographs sum (dwell time)
    #sum(|tref-tmon|/tmon)
    def monographs(self,userno):
        j = userno * n
        answer = 0
        for i in range(1,n):
            answer += abs(self.dwell1[i]-self.dwell1[j+i])/self.dwell1[j+i]
        return answer

    def deviation(self,userno):
        d = ((self.digraphs(userno)/(n-1)) + (self.monographs(userno)/n))*50
        return d

    def fr(self,userno):
        return self.deviation(userno) >= threshold

    def fa(self,userno):
        return self.deviation(userno) <= threshold

user = User()
user.loadfile("Lab2-Sample-Files\User1.txt")
print(user.fly[0],user.fly[2999])
print(user.deviation(1),user.deviation(2),user.deviation(3),user.deviation(4),user.deviation(5))
