my_list = []

def add_value(value):
    my_list.append(value)

def remove_value(value):
    my_list.remove(value)

add_value(5)
add_value(10)
add_value(15)

remove_value(10)

count = len(my_list)
print("სიაში არსებული მნიშვნელობების რაოდენობა:", count)

add_value(20)
print("სიაში ახალი მნიშვნელობის დამატება მეორე ინდექსზე:", my_list)




''' შექმენით სია, რომელშიც დაამატებთ მნიშვნელობას სიის ბოლოში, შემდეგ ამოშლით ნებისმიერ მნიშვნელობას
 და მაგის შემდგომ  გაიგებთ ამ სიაში არსებული მნიშვნელობების რაოდენობას და შემდეგ ჩაამატებთ
 ახალ მნიშვნელობას მეორე ინდექსზე '''
