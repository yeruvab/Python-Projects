def game_over(matrix):
    
    X = ['x','x','x']
    O = ['o','o','o']
    
    for i in range(3):
        temp1 = []
        temp2 = []
        
        for j in range(3):
            temp1.append(matrix[i][j])
            temp2.append(matrix[j][i])
            
        if X == temp1 or X == temp2:
            return True
        
        if O == temp1 or X == temp2:
            return True

    temp3 = []
    
    for ij in range(3):
        temp3.append(matrix[ij][ij])

        if X == temp3:
            return True
        
        if O == temp3:
            return True

    temp4 = []
    i = 0
    j = len(matrix)-1
    
    while i < len(matrix) and j > -1:
        temp4.append(matrix[i][j])
        i += 1
        j -= 1
    
    if X == temp4:
        return True
    
    if O == temp4:
        return True

def user1(u1):
    
    x_y = input('\n{}: Enter position in the format(x,y): '.format(u1))
    x = int(x_y[0])
    y = int(x_y[2])
    return x,y

def user2(u2):
    
    x_y = input('\n{}: Enter position in the format(x,y): '.format(u2))
    x = int(x_y[0])
    y = int(x_y[2])
    return x,y


def main():
    matrix = [['-','-','-'],['-','-','-'],['-','-','-']]

    u1 = input('Enter User 1 name: ')
    u2 = input('Enter User 2 name: ')
    
    while game_over(matrix) == None:
        
        x,y = user1(u1)
        matrix[x][y] = 'x'
        
        if game_over(matrix) == True:
            print('\n{} is the winner!'.format(u1))
            break

        print('\n')
        for line in matrix:
            print(line[0],line[1],line[2])
            
        x,y = user2(u2)
        matrix[x][y] = 'o'

        if game_over(matrix) == True:
            print('\n{} is the winner!'.format(u2))
            break

        print('\n')
        for line in matrix:
            print(line[0],line[1],line[2])
            
        
if __name__ == main():
    main()
