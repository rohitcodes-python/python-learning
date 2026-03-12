list=[1,5,6,7,15,14]
largest=list[0]
sec_largest=list[0]

for item in list:
  if item>largest:
    sec_largest=largest
    largest=item
  elif item>sec_largest:
    sec_largest=item
    
print(largest)
print(sec_largest)
