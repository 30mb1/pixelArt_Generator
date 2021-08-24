import os

dir1 = "source/head"
list = os.listdir(dir1)
number_of_head = len(list)

dir2 = "source/glasses"
list = os.listdir(dir2)
number_of_glasses = len(list)

dir3 = "source/background"
list = os.listdir(dir3)
number_of_background = len(list)

dir4 = "source/body"
list = os.listdir(dir4)
number_of_body = len(list)

dir5 = "source/scarf"
list = os.listdir(dir5)
number_of_scarf = len(list)

dir6 = "source/shirt"
list = os.listdir(dir6)
number_of_shirt = len(list)

TOTAL = number_of_body*number_of_shirt*number_of_scarf*number_of_head*number_of_glasses*number_of_background