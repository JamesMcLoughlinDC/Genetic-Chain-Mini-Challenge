# ask user to input the grid size from the command line
n = int(input("Enter the size of the grid: "))

# Initialize an n X n empty matrix
matrix = [[ ' ' for i in range(n)] for i in range(n)]

#Set upper limit(UL) and lower limit(LL) for the boundaries of our spiral
LL = 0
UL = n

#continue the process below until the UL is less than or equal to LL,
#.. at which point our spiral would cross itself, so we need to stop.
while LL < UL:
    #Iterate from left ->right along row
    for col in range(LL,UL):
        matrix[LL][col]="*"
    LL +=1 
    UL -=1

    #iterate from top -> botton along column
    for row in range(LL,UL):
        matrix[row][UL] = "*"
    LL+=1

    #Iterate from right ->left along row
    for col in range(LL,UL):
        matrix[n-LL][col]="*"
    UL -=1

    #iterate from botton -> top along column
    for row in range(LL,UL):
        matrix[row][n-UL] = "*"

#turn entries into a string so they print out with better formatting... 
#Could also just print row by row if unconcernted with matching origina formatting
for row in matrix: 
    temp = ""
    for col in row: 
        temp = temp +" "+ col
    print("[" + temp+ "]")


