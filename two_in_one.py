def convert(array):
    monodimensional_array = []
    for i in range(0, 16):
        if i % 2 == 0:
            for j in array[i]:
                monodimensional_array.append(j)   
        else:
            for j in array[i][::-1]:
                monodimensional_array.append(j)
    return monodimensional_array

if __name__ == '__main__':
   # print('Run from another module')
   print(convert([[1,0,1],[1,0,1],[1,0,1]]))
