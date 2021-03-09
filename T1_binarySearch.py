def binarySearch(array, start, end, element):
  if start > end:
    return -1
  else:
    mid = (start+end)//2
    if element == array[mid]:
      return mid
    elif element < array[mid]:
      return binarySearch(array, start, mid-1, element)
    else:
      return binarySearch(array, mid+1, end, element)

# Test function (Element in the array)
array = [3, 5, 6, 9, 20]
desiredElement = 5
result = binarySearch(array, 0, len(array)-1, desiredElement)

print("Search for",desiredElement, "in the array:",array)
if result == -1:
  print("Element", desiredElement, "is not in the array.")
else:
  print("Element", desiredElement, "is in index",result)

# Test function (Element not in the array)
desiredElement = 66
result = binarySearch(array, 0, len(array)-1, desiredElement)

print("\nSearch for",desiredElement, "in the array:",array)
if result == -1:
  print("Element", desiredElement, "is not in the array.")
else:
  print("Element", desiredElement, "is in index",result)
