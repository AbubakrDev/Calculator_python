start = input('Boshlash uchun ha ni yozing bolamasa yoqni yozing:').lower()

while start == 'ha':
    num = int(input('Birinchi sonni kiriting:'))
    num2 = int(input('Ikkinchi sonni kiriting:'))
    why = input('Amalni kiriting:')
    if why == '+':
        print(f'Sizning natijangiz:{num + num2}')
    elif why == '-':
        print(f'Sizning natijangiz:{num - num2}')
    elif why == '*':
        print(f'Sizning natijangiz:{num * num2}')
    elif why == '/':
        print(f'Sizning natijangiz:{num / num2}')
    else:
        print('Kiritgan amalingiz notogri boshqa amalni kiriting:')
    start = input('Takrorlash uchun ha ni yozing bolamasa yoqni yozing:').lower()
