'''3)   მომხმარებელს შემოატანიეთ რიცხვი და for loop-ის დახმარებით დაპრინტეთ რიცხვები 1-დან 
მომხმარებლის მიერ შემოტანილი რიცხვის ჩათვლით.
ტერმინალში გამოიტანეთ ამ რიცხვების ჯამი და საშუალო არითმეტიკული'''
number = int(input('Enter your number: '))
sum = 0
for i in range(1, number + 1):
    sum += i
    print(sum)