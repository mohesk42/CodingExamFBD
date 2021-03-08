#Mohammad Eskandarani

def replaceAll(txt, old, new):
  if len(old) == 0:
    return txt
  if txt == '':
    return ''
  if txt[:len(old)] == old:
    return new + replaceAll(txt[len(old):], old, new)
  return txt[0] + replaceAll(txt[1:], old, new)

# Test function
txt = "Hello World!"
old = "o"
new = "Z"
result = replaceAll(txt, old, new)
print("Before:", txt)
print("After replacing", old, "with", new)
print(result)

txt = "My name is Fahd"
old = "Fahd"
new = "Mohammad"
result = replaceAll(txt, old, new)
print("\nBefore:", txt)
print("After replacing", old, "with", new)
print(result)