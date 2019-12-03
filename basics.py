c = 'g'

def convertToASIC(string):
 for x in string:
  return ord(x)

print(convertToASIC(c))

value = 0
name = "frontDoor"

sql = "UPDATE doors SET value = '"+str(value)+"' WHERE name = '"+str(name)+"'"
print(sql)