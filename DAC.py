#Question 3.1

#Global Dict. and Access Control Matrix
perm = {0: ' - ', 1: ' r ', 2: ' w ', 3 : ' rw', 4 : ' rx', 5 : 'rwx'}
users = {'User1':0, 'User2':1, 'User3':2, 'User4':3,'User5':4}
files = {0 : 'File1', 1 : 'File2', 2 : 'File3', 3 : 'File4', 4 : 'File5', 5 : 'File6'}

matrix = [[5,5,5,5,5,5],
          [3,0,4,0,1,0],
          [0,0,3,3,0,0],
          [4,0,0,1,1,0],
          [0,5,0,0,1,0,1]   
          ]

#Main Menu 
def main():
    print("\nMain Menu\nOptions \n 1-Print User Priveleges \n 2-Change Priv\n 3-Print Matrix\n 4-Exit")
    option = int(input())
    if option == 1:
        printPriv()
    elif option == 2:
        changePriv()
    elif option == 3:
        printMatrix()
    
#Change Privelage of current user
def changePriv():
    print("Enter the file you wish to change: File1-0   File2-1   File3-2   File4-3   File5-4   File6-5")
    fileNo = int(input())
    print("Change access to: None-0   r-1   w-2   rw-3   rx-4   rwx-5")
    newPriv = int(input())
    matrix[user][fileNo] = newPriv
    if __name__ == "__main__":
        main()

#Authorize the users request (not working yet)
def authorize(request):
    if matrix[user][request] == 0:
        return False
    else:
        return True
    

#Print matrix 
def printMatrix():
    print("       |F1   |F2   |F3   |F4   |F5   |F6 \n")
    print(" User1 | "+perm.get(matrix[0][0])+" | "+perm.get(matrix[0][1])+" | "+perm.get(matrix[0][2])+" | "+perm.get(matrix[0][3])+" | "+perm.get(matrix[0][4])+" | "+perm.get(matrix[0][5]))
    print(" User2 | "+perm.get(matrix[1][0])+" | "+perm.get(matrix[1][1])+" | "+perm.get(matrix[1][2])+" | "+perm.get(matrix[1][3])+" | "+perm.get(matrix[1][4])+" | "+perm.get(matrix[1][5]))
    print(" User3 | "+perm.get(matrix[2][0])+" | "+perm.get(matrix[2][1])+" | "+perm.get(matrix[2][2])+" | "+perm.get(matrix[2][3])+" | "+perm.get(matrix[2][4])+" | "+perm.get(matrix[2][5]))
    print(" User4 | "+perm.get(matrix[3][0])+" | "+perm.get(matrix[3][1])+" | "+perm.get(matrix[3][2])+" | "+perm.get(matrix[3][3])+" | "+perm.get(matrix[3][4])+" | "+perm.get(matrix[3][5]))
    print(" User5 | "+perm.get(matrix[4][0])+" | "+perm.get(matrix[4][1])+" | "+perm.get(matrix[4][2])+" | "+perm.get(matrix[4][3])+" | "+perm.get(matrix[4][4])+" | "+perm.get(matrix[4][5]))
    if __name__ == "__main__":
        main()
        
#Print the users file access privelages 
def printPriv():
##    print("\nEnter User")
##    user = users.get(input())
    print ("Type corresponding number to open file: File1:0    File2:1    File3:2    File4:3    File5:4    File6:5")
    fileNo = int(input())

    
    if authorize(fileNo):
        print("Your {0} access request to the file {1} is granted".format(perm.get(matrix[user][fileNo]), files.get(fileNo)))
    else:
        print("You only have {0} access rights to the file {1}".format(perm.get(matrix[user][fileNo]), files.get(fileNo)))
    
    if __name__ == "__main__":
        main()
    
def starthere():
    print("Please enter username")
    user = users.get(input())
    main()

"""
#Runs main function the first time 
if __name__ == "__main__":
    starthere()
""" 
