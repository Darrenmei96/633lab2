#Question 3.2 

roles = { 'Manager':0 , 'Technical Staff': 1 ,'Sales' : 2}

perm = {0: ' - ', 1: ' r ', 2: ' w ', 3 : ' rw', 4 : ' rx', 5 : 'rwx'}
users = {'User1':roles['Manager'], 'User2':roles['Technical Staff'], 'User3':roles['Technical Staff'], 'User4':roles['Sales'],'User5':roles['Sales']}
files = {0 : 'File1', 1 : 'File2', 2 : 'File3', 3 : 'File4', 4 : 'File5', 5 : 'File6'}
matrix = [[5,5,5,5,5,5],
          [3,0,4,0,1,0],
          [0,0,3,3,0,0]
          ]

#Main function, runs appropriate functions 
def main():
    print("Main Menu:\n1-Print Current User Role\n2-Change User Access\n3-Print Matrix")
    opion = int(input())
    if option == 1:
        printrole()
    elif option == 2:
        assign()
    


matrix[roles[user]][request]
#Assign User a roles, if already has a role, changes it 
##def assign():
##    print("Assign Menu:\n1-Assign Role to different User \n2-Change Current Role")
##    option = int(input())
##    if option == 1:
        
            
        
        

    
    
#Prints the current user's role 
def printRole():
    print("")
    print("")
    
    

##def userCheck(user):
    

print("Enter your username")
user = int(input())
main()
