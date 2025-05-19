#('leftwidth','rightwidth')
#p33icnic_items={'sandwich':20,'waterbottle':10,'samosa':15}
#for k,v in picnic_items.items():
 #   print(k.lstrip(5)+str(v).rjust(3,'\n'))
import pyperclip
pyperclip.copy('''The pyperclip module has copy() and paste() functions that can send text to and 
receive text from your computer’s clipboard. 
➢ Of course, if something outside of your program changes the clipboard contents, the 
paste() function will return it. 
1.3  Project: Password Locker''')
print(pyperclip.paste())