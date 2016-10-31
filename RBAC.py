#Question 3.2 

roles = {0 : 'Manager', 1 : 'Technical Staff', 2 : 'Sales'}

perm = {0: ' - ', 1: ' r ', 2: ' w ', 3 : ' rw', 4 : ' rx', 5 : 'rwx'}
users = {'User1':0, 'User2':1, 'User3':2, 'User4':3,'User5':4}
files = {0 : 'File1', 1 : 'File2', 2 : 'File3', 3 : 'File4', 4 : 'File5', 5 : 'File6'}
matrix = [[5,5,5,5,5,5],
          [3,0,4,0,1,0],
          [0,0,3,3,0,0],
          [4,0,0,1,1,0],
          [0,5,0,1,0,1]   
          ]

class User:
#Main function, runs appropriate functions 
def main():
    print("Main Menu:\n1-Print Current User Role\n2-Change User Access\n3-Print Matrix")
    opion = int(input())
    if option == 1:
        printrole()
    elif option == 2:
        assign()
    


#Assign User a roles, if already has a role, changes it 
def assign():
    print("Assign Menu:\n1-Assign Role to different User \n2-Change Current Role")
    option = int(input())
    if option == 1:
        
        

    
    
#Prints the current user's role 
def printRole():
    print("")
    print("")
    
    

def userCheck(user):
    

if __name__ == "__main__":
          print("Enter your username")
          user = int(input())
          main()
