class Node(object): #класс узла
        def __init__(self, data):
          self.data = data
          self.next = None
        
class LinkedList(object): #класс односвязного списка
       def __init__(self, *values):
          if len(values) == 0:
              self.size = 0
              self.head = None
          elif len(values) == 1:
              self.size = 1
              self.head = Node(values[0])
          else:
              self.size = len(values)
              self.head = Node(values[0])

              current_node = self.head
              for i in range(1, len(values)):
                  new_node = Node(values[i])
                  current_node.next = new_node
                  current_node = new_node

       def __del__(self):
          self = None

       def __getitem__(self, index):
           if self.size == 0:
               raise IndexError("list is empty")
           
           current_node = self.head
           i = 0
           if isinstance(index, slice): #проверка на срез
               if (index.start < 0) or (index.stop < 0):
                   raise IndexError("index must be positive")

               if index.start > index.stop:
                   raise IndexError("start index must be less stop index")

               try:
                   if index.step <= 0:
                       raise IndexError("step must be above zero")
               except TypeError:
                   pass

               list = []
               while (current_node.next and i != index.start):
                   current_node = current_node.next
                   i += 1
               
               step = index.step
               if index.step == None:
                   step = 1

               while (current_node.next and i != index.stop):
                   if ((i - index.start) % step) == 0:
                       list.append(current_node.data)
               
                   current_node = current_node.next

                   i += 1

               if (i < index.stop) and (((i - index.start) % step) == 0):
                   list.append(current_node.data)

               return list     
           elif isinstance(index, int):    
               if index > self.size - 1:
                  raise IndexError("list index out of range")
           
               if index < 0:
                  raise IndexError("list index must be positive")
           
               if index == 0:
                   return current_node.data

               while (current_node.next):
                   current_node = current_node.next
                   i += 1
                   if i == index:
                      return current_node.data
           else:
               raise TypeError("list indices must be integers or slices")
               
       def __setitem__(self, index, value):
           current_node = self.head
           i = 0
           if isinstance(index, slice): #проверка на срез
               try:
                   iter(value)
               except TypeError:
                   raise TypeError ("can only assign an iterable")

               if (index.start < 0) or (index.stop < 0):
                   raise IndexError("index must be positive")

               if index.start > index.stop:
                   raise IndexError("start index must be less stop index")

               try:
                   if index.step <= 0:
                       raise IndexError("step must be above zero")
               except TypeError:
                   pass
               
               step = index.step
               if index.step == None:
                   step = 1  

               start = index.start 
               if index.start > (self.size - 1): #если стартовый индекс больше размера массива начинаем с последнего элемента
                   start = self.size - 1    

               if (len(value) > (index.stop - start) // step):
                   raise ValueError("attempt to assign sequence of size" + str(len(value)) + "to extended slice of size " + str((index.stop - start) // step))
               
               self.size += len(value)

               while (current_node.next and i != start):
                   current_node = current_node.next
                   i += 1

               value = list(value)
               i_value = 0 

               if self.size == 0:
                   self.head = Node(value[0]) 
                   i_value += 1
                   current_node = self.head

               while (i != index.stop):
                   if ((i - start) % step) == 0:
                       if current_node.next == None:
                           try:
                               current_node.next = Node(value[i_value])
                           except IndexError:
                               return 
                       else: 
                           try:
                              current_node.data = value[i_value]
                           except IndexError:
                              return 
                       i_value += 1

                   if current_node.next == None:
                       return    
               
                   current_node = current_node.next

                   i += 1

               if (i < index.stop) and (((i - start) % step) == 0):
                   try:
                       current_node.data = value[i_value]
                   except IndexError:
                       return   
           elif isinstance(index, int):
               if self.size == 0:
                  raise IndexError("list is empty")
               
               if index > self.size - 1:
                  raise IndexError("list index out of range")
           
               if index < 0:
                  raise IndexError("list index must be positive")
               
               self.size += 1
           
               if index == 0:
                   return current_node.data

               while (current_node.next):
                   current_node = current_node.next
                   i += 1
                   if i == index:
                      current_node.data = value
           else:
               raise TypeError("list indices must be integers or slices")
           
       def __str__(self):
           list = []
           if self.size == 0:
              return str(list)
           
           current_node = self.head
           while (current_node.next):
               list.append(current_node.data)
               current_node = current_node.next

           list.append(current_node.data)

           return str(list)
                   
       def __len__(self):
           return self.size    
               
       def append(self, *values):
          self.size += len(values)

          new_node = Node(values[0])

          if self.size == 0:
              self.head = new_node
              
          current_node = self.head
          while (current_node.next):
              current_node = current_node.next

          current_node.next = new_node    
          for i in range(1, len(values)):
              new_node = Node(values[i])
              current_node.next = new_node
              current_node = new_node

       def index(self, value):
           if self.size == 0:
               raise ValueError("list is empty")
           
           current_node = self.head
           i = 0
           while (current_node.next):
               if current_node.data == value:
                   return i
               
               current_node = current_node.next
               i += 1

           if current_node.data == value:
                   return i
           
           raise ValueError(str(value) + " is not in list")
       
       def remove(self, value):
           if self.size == 0:
               raise IndexError("list is empty")

           current_node = self.head
           if current_node.data == value:
                  self.head = current_node.next 
                  self.size -= 1 
                  return
           
           previous_node = current_node #записываем предыдущий элемент
           current_node = current_node.next #записываем текущий элемент
           while (current_node.next):
               if current_node.data == value:
                   previous_node.next = current_node.next
                   self.size -= 1
                   return
               previous_node = current_node
               current_node = current_node.next

           if current_node.data == value:
               previous_node.next == None
               self.size -= 1
               return
           
           raise ValueError(str(value) + " is not in list")
                      
       def pop(self, index = None):
           if self.size == 0:
               raise IndexError("list is empty")

           if index == None:
               index = self.size - 1

           if not isinstance(index, int):
               raise TypeError("index must be integer")    

           if index < 0:
               raise IndexError("index must be positive")
           
           if index > (self.size - 1):
               raise IndexError("index out of range")
           
           current_node = self.head
           i = 0
           if i == index:
                  res = current_node.data
                  self.head = current_node.next 
                  self.size -= 1 
                  return res

           previous_node = current_node #записываем предыдущий элемент
           current_node = current_node.next #записываем текущий элемент
           i += 1
           while (current_node.next):
               if i == index:
                   res = current_node.data
                   previous_node.next = current_node.next
                   self.size -= 1
                   return res
               previous_node = current_node
               current_node = current_node.next
               i += 1

           if i == index:
               res = current_node.data
               previous_node.next = None
               self.size -= 1
               return res

       def insert(self, index, *values):
           if index == None:
               index = self.size - 1

           if not isinstance(index, int):
               raise TypeError("index must be integer")

           i_start = 0 
           if self.size == 0 and index != 0:
               raise IndexError("list is empty")
           elif self.size == 0 and index == 0:
               self.head = Node(values[0])
               i_start = 1   

           if index < 0:
               raise IndexError("index must be positive")
           
           if (index > (self.size - 1) and self.size != 0) or (index > 0 and self.size == 0): #проверяем не вышел ли индекс за границы списка или если список пустой не больше ли индекс 0
               raise IndexError("index out of range")
           
           current_node = self.head
           i = 0

           while (i != index - 1 and index != 0):
               current_node = current_node.next
               i += 1

           next = current_node.next #сохраняем ссылку на следующий элемент после вставки

           for i in range(i_start, len(values)):
               current_node.next = Node(values[i])
               current_node = current_node.next

           current_node.next = next

           self.size += len(values)

       def swap(self, index1, index2):
           if self.size == 0:
               raise IndexError("list is empty")

           if (index1 > self.size - 1) or (index2 > self.size - 1):
               raise IndexError("list index out of range")

           if (index1 < 0) or (index2 < 0):
               raise IndexError("index must be positive")

           Node_head = None
           Node1_prev = None
           Node2_prev = None 
           current_node = self.head
           i = 0
           if (index1 == 0) or (index2 == 0): #еси один из индексов 0 отдельно сохраняем указатель на начало списка
               Node_head = self.head
               current_node = current_node.next
               i = 1

           while (current_node.next):
               if (i == index1 - 2):
                   Node1_prev = current_node.next
               if (i == index2 - 2):
                   Node2_prev = current_node.next
               current_node = current_node.next
               i += 1 

           if (i == index1 - 2):
               Node1_prev = current_node.next
           if (i == index2 - 2):
               Node2_prev = current_node.next       

           if Node_head == None: #случай когда нужно менять любые два элемента кроме головного
               temp = Node1_prev.next
               Node1_prev.next = Node2_prev.next
               Node2_prev.next = temp

               temp = Node1_prev.next.next
               Node1_prev.next.next = Node2_prev.next.next
               Node2_prev.next.next = temp
           else: #случай когда нужно поменять головной элемент местами с другим
               if Node1_prev == None:
                   #сначала меняем ссылки на следующий элементы
                   temp = Node2_prev.next.next
                   Node2_prev.next.next = Node_head.next
                   Node_head.next = temp

                   #потом меняем ссылки на сами элементы 
                   self.head = Node2_prev.next
                   Node2_prev.next = Node_head
               elif Node2_prev == None:
                   temp = Node1_prev.next.next
                   Node1_prev.next.next = Node_head.next
                   Node_head.next = temp 
                   
                   self.head = Node1_prev.next
                   Node1_prev.next = Node_head             
                          
       def clear(self):
           self.size = 0
           self.head = None

print("Инициализация списка и вывод с помощью print: ")
lList = LinkedList(1, 2)
print(lList)

print("\nУстановка элементов с помощью индекса/среза: ")
lList[3:6] = [3,4]
print(lList)

print("\nДоступ к элементу по индексу/срезу: ")
print(lList[2])

print("\nПолучение длины списка len(): ")
print(len(lList))

print('\nДобавление эллемента(ов) в конец списка методом append(5, "arr"): ')
lList.append(5, "arr")
print(lList)

print('\nНахождение индекса элемента методом index("arr"): ')
print(lList.index("arr"))

print("\nУдаление эллемента из списка по значению методом remove(1):")
lList.remove(1)
print(lList)

print("\nУдаление эллемента из списка по индексу/последнего элемента методом pop(2):")
lList.pop(2)
print(lList)

print("\nВставка эллемента(ов) в список по индексу (элементы правее сдвигаются) методом insert(1, 3, 5, [1,3,4]):")
lList.insert(1, 3, 5, [1,3,4])
print(lList)

print("\nЗамена местами двух элементов из списка по их индексам методом swap(0, 3):")
lList.swap(0, 3)
print(lList)

print("\nУдаление всех элементов списка методом clear():")
lList.clear()
print(lList)

print("\nУдаление списка: ")
del lList
print(lList) 