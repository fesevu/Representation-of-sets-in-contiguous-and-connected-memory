class Array(object):
          types = {
                  int: float,
                  float: float,
                  str: str,
                  list: list,
                  dict: dict,
                  tuple : tuple,
                  set: set,
                  bool: bool,
                  None: None      
          }

          def __init__(self, size, type = None):
                    self.size = size
                    try:
                              self.type = self.types[type]
                    except KeyError:
                            self = None
                            print("TypeError: type must be one of available types")
                            return    

                    try:  
                              self.array = [None] * size
                    except MemoryError:
                            self = None
                            print("MemoryError: size is too big")
          """""
          второй вариант инициализации
          def __init__(self, *values):
                    self.array = [value for value in values]
                    self.size = 0
                    i = 0
                    flag = True
                    while (flag):
                              try:
                                    self.array[i]
                                    i += 1
                                    self.size += 1
                              except IndexError:
                                      flag = False
          """
          

          def __del__(self):
                  self = None

          def __getitem__(self, index):
                    try:
                              return self.array[index]
                    except:
                            print("IndexError: array index out of range")

          def __setitem__(self, index, value):
                    value1 = value
                    if isinstance(value, (list, dict, tuple, set)): #если вводят несколько эллементов проверяем одного ли типа они
                            value = list(value)
                            for i in range(1, len(value)):
                                    if not (isinstance(value[i], type(value[i-1]))):
                                            print("TypeError: type of all elements must be same")
                                            return
                                    
                            value1 = value[0]
   
                    if self.type == None:
                            self.type = self.types[type(value1)]

                    if self.types[type(value1)] == self.type:  #проверяем является ли тип элемента(ов) таким же как тип всего массива
                              try:
                                        self.array[index] = value
                              except IndexError:
                                        print("IndexError: array index out of range")
                    else:
                              #raise TypeError("Only numeric values are allowed")
                              print("TypeError: Only same type of array are allowed") 
                            
          def __str__(self):
                    return str(self.array)

          def __len__(self):
                    return self.size

          def swap(self, index1, index2):
                    try:
                              temp = self.array[index1]
                    except IndexError:
                            print("IndexError: array index out of range")  
                            return 

                    try:
                               self.array[index1] = self.array[index2]
                    except IndexError:
                            print("IndexError: array index out of range")  
                            return

                    try:
                              self.array[index2] = temp
                    except IndexError:
                            print("IndexError: array index out of range")  
                            return       
                            
          def index(self, value, start = 0, end = None):
                    try:
                            if end == None:
                                        end = self.size
                            elif end < 0:
                                    end = self.index(self.array[end])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range end index")
                            return -1

                    try:
                            if start < 0:
                                    start = self.index(self.array[start])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range start index")
                            return -1
                    
                    if start > end:
                              print("IndexError: start index > end index")
                              return -1
                    
                    for i in range (int(start), int(end)):
                              if self.array[i] == value:
                                        return i
                              
                    print("ValueError: " + str(value) + " not in list")

          def getValues(self, start = 0, end = None):
                    try:
                            if end == None:
                                        end = self.size
                            elif end < 0:
                                    end = self.index(self.array[end])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range end index")
                            return -1

                    try:
                            if start < 0:
                                    start = self.index(self.array[start])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range start index")
                            return -1
                    
                    if start > end:
                              print("IndexError: start index > end index")
                              return -1
                    
                    arr = Array(int(end) - int(start))
                    for i in range(int(start), int(end)):
                              arr[i - int(start)] = (self.array[i])

                    return arr

          def setValue(self, start, end, *values):
                    if len(values) > self.size:
                              print("TypeError: setValue() takes size of array arguments but were given more")
                              return -1
                    elif len(values) <= 0:
                              print("TypeError: setValue() takes size of array arguments but were given 0")
                              return -1
                    elif len(values) > end - start + 1:
                              print("TypeError: setValue() takes range of array arguments but were given more")
                              return -1
                    elif len(values) < end - start + 1:
                              print("TypeError: setValue() takes range of array arguments but were given less")
                              return -1
                    
                    try:
                            if end == None:
                                        end = self.size
                            elif end < 0:
                                    end = self.index(self.array[end])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range end index")
                            return -1

                    try:
                            if start < 0:
                                    start = self.index(self.array[start])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range start index")
                            return -1
                    
                    if start > end:
                              print("IndexError: start index > end index")
                              return -1
                    
                    if len(values) > 1:
                            for i in range(1, len(values)):
                                    if not (isinstance(values[i], type(values[i-1]))):
                                            print("TypeError: type of all elements must be same")
                                            return
                                    
                    if self.types[type(values[0])] != self.type:
                            print("TypeError: Only same type of array are allowed")
                            return
                    
                    for i in range(start, end):
                              self[i] = values[i - start]

          def printValues(self, start = 0, end = None):
                    try:
                            if end == None:
                                        end = self.size
                            elif end < 0:
                                    end = self.index(self.array[end])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range end index")
                            return -1

                    try:
                            if start < 0:
                                    start = self.index(self.array[start])
                    except TypeError:
                            print("TypeError")
                            return -1
                    except IndexError:
                            print("IndexError: array index out of range start index")
                            return -1
                    
                    if start < end:
                        for i in range(start, end):
                              print(self.array[i], end=' ')
                    else:
                        for i in range(start, end, -1):
                              print(self.array[i], end=' ')

                    print()
                  

arr = Array(4)

for i in range(len(arr)):
        arr[i] = i

print("gettitem: ")
print(arr[1])

print("\nPrint: ")
print(arr)

print("\nLen: ")
l = len(arr)
print(l)

print("\nSwap: ")
arr.swap(0, 2)
print(arr)

print("\nIndex элемента: ")
index1 = arr.index(2)
print(index1)

print("\nIndex элемента в промежутке: ")
index2 = arr.index(1, 1, 3)
print(index2)

print("\nIndex элемента начиная с индекса: ")
index3 = arr.index(0, 2)
print(index3)

print("\nПолучение элементов в промежутке: ")
print(arr.getValues(1,3))

print("\nСрез [0:4:2]: ")
print(arr[0:4:2])

print("\nУстановка элементов в промежутке: ")
arr.setValue(2,3,7,"arr")
arr.printValues(3, 1)

print("\nУдаление массива: ")
del arr
print(arr) #должна выводиться ошибка, try except не использовался