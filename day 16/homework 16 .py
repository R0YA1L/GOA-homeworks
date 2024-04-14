point = int(input('Enter your point: '))
if point > 90 and point < 100:
    print('თქვენ დაგიფინანსდათ სწავლა სრულიად.')
if point > 70 and point < 90:
    print('თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით.')
if point > 40 and point < 70:
    print('თქვენ დაგიფინანსდებათ სწავლა 500 ლარით.')
if point < 40:
    print('თქვენ სწავლა არ დაგიფინანსდებათ!!!')