row1 = ['11','21','31']
row2 = ['12','22','32']
row3 = ['13','23','33']
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure? ')

column = int(position[0])
row = int(position[1])
map[row-1][column-1] = 'X'
print(f'{row1}\n{row2}\n{row3}')
