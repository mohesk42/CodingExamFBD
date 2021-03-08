#Mohammad Eskandarani

def getUniques(array):
  uniques = []
  for i in range(len(array)):
    u = True
    for j in range(len(array)):
      if array[i] == array[j] and i!=j:
        u = False
    
    if u:
      uniques.append(array[i])
  return uniques

# Test function:
array1 = [4,3,6,6,1]
uniques1 = getUniques(array1)
print("Array 1 =", array1)
print("Result:", uniques1)

array2 = [1,1,2,3,3]
uniques2 = getUniques(array2)
print("\nArray 2 =", array2)
print("Result:", uniques2)

array3 = [1]
uniques3 = getUniques(array3)
print("\nArray 3 =", array3)
print("Result:", uniques3)