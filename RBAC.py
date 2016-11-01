#Question 3.2 

roles = { 'Manager':1, 'Technical Staff':2 , 'Sales':3}
#roles = { 1:'Manager', 2:'Technical Staff' , 3:'Sales'}

perm = {0: ' - ', 1: ' r ', 2: ' w ', 3 : ' rw', 4 : ' rx', 5 : 'rwx'}
users = {'User1':'Manager', 'User2':'Technical Staff', 'User3':'Technical Staff', 'User4':'Sales','User5':'Sales'}
files = {0 : 'File1', 1 : 'File2', 2 : 'File3', 3 : 'File4', 4 : 'File5', 5 : 'File6'}
matrix = [[5,5,5,5,5,5],
          [3,0,4,0,1,0],
          [0,0,3,3,0,0]
          ]

#Main function, runs appropriate functions 
def main():
    print("Main Menu:\n1-Print Current User Role\n2-Change User Access\n3-Print Matrix")
    option = int(input())
    if option == 1:
        printRole()
    elif option == 2:
        assign()
    elif option == 3:
        printMatrix()



##matrix[roles[user]][request]
##Assign User a roles, if already has a role, changes it 
def assign():
    print("Assign Menu:\n1-Assign Role to different User \n2-Change Current Role")
    option = int(input())
##    if option == 1:
        
        
            
        
        

def printMatrix():
    print("       |F1   |F2   |F3   |F4   |F5   |F6 \n")
    print(" Mng.  | "+perm.get(matrix[0][0])+" | "+perm.get(matrix[0][1])+" | "+perm.get(matrix[0][2])+" | "+perm.get(matrix[0][3])+" | "+perm.get(matrix[0][4])+" | "+perm.get(matrix[0][5]))
    print(" Tech  | "+perm.get(matrix[1][0])+" | "+perm.get(matrix[1][1])+" | "+perm.get(matrix[1][2])+" | "+perm.get(matrix[1][3])+" | "+perm.get(matrix[1][4])+" | "+perm.get(matrix[1][5]))
    print(" Sales | "+perm.get(matrix[2][0])+" | "+perm.get(matrix[2][1])+" | "+perm.get(matrix[2][2])+" | "+perm.get(matrix[2][3])+" | "+perm.get(matrix[2][4])+" | "+perm.get(matrix[2][5]))

    
#Prints the current user's role 
def printRole():
    k = users[user]
    print(k)
    
    

##def userCheck(user):
    

print("Enter your username")
user = input()
main()
