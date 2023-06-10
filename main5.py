dba = [{'name': 'Твоя2 Улыбка', 'url': 'smile-nk.ru', 'phone1': '+7 (3843) 20-07-77', 'phone2': '+7 (905) 907-00-55', 'phone3': '', 'phone4': '', 'tg': '', 'tg2': '', 'chat': '', 'vk': 'vk.com/smilenk', 'email': ''}, {'name': 'Твоя Улыбка', 'url': 'smile-nk.ru', 'phone1': '+7 (3843) 20-07-77', 'phone2': '+7 (905) 907-00-55', 'phone3': '', 'phone4': '', 'tg': '', 'tg2': '', 'chat': '', 'vk': 'vk.com/smilenk', 'email': ''}]

with open('test.txt', 'a', encoding='utf8') as f3:
    for w in range(len(dba)):
        for i, x in dba[0].items():
            f3.write(f'{i}: {x}, ')
        f3.write('\n')
