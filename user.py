class User:
    def __init__(filename):
        self.key1 = []
        self.key2 = []
        self.fly = []
        self.dwell1 = []
        self.dwell2 = []
        loadfile(filename)

    def loadfile(filename):
        #read all the lines
        #note that the first line[0] includes the header
        with open(filename, "r") as lines:
            for line in lines:
                array = line.split()
                key1.append(array[0])
                key2.append(array[1])
                fly.append(array[2])
                dwell1.append(array[3])
                dwell2.append(array[4])
        lines.close()

    # Calculate the digraphs sum (fly time)
    #sum(|tref-tmon|/tmon)
    def digraphs(setnumber):
        j = setnumber * 500
        answer = 0;
        for i in range(1,501):
            answer += abs(self.fly[i]-self.fly[j])/self.fly[j]
        return answer

    # Calculate the monographs sum (dwell time)
    #sum(|tref-tmon|/tmon)
    def monographs(setnumber):
        j = setnumber * 500
        answer = 0;
        for i in range(1,501):
            answer += abs(self.dwell[i]-self.dwell[j])/self.dwell[j]
        return answer
