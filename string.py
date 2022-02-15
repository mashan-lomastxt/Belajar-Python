print("Hello world!")

# mengakses nilai dalam String
name = "John" 
message = "Hello, " + name + "!"
print("name:[0] ", name[0])
print("message[1:4]: ", message[1:4])

# update String
message = "Hello World!"
print("Update String:-",message[:6] + "Python")

# triple Quote Python
kutipantiga = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (kutipantiga)