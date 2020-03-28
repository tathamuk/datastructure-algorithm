from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your filename %r:" %filename)

print (txt.read())

print ("Typer the filename again:")
file_again = input(">")

txt_again = open (file_again)

print (txt_again.read())
