import json
import requests
chats = ['replain', 'intercom', 'getinchat', 'profeat', 'crisp', 'convead', 'freshworks', 'chatra', 'callibri', 'multichat', 'threads', 'cleversite', 'front.com', 'drift', 'webim', 'omnidesk', 'textback', 'chatmanager', 'chatbro', 'verbox', 'smartsupp', 'jivo', 'mango-office', 'mango-chat', 'teletype', 'sender', 'livetex', 'redhelper', 'talk-me', 'tinkoff', 'envybox', 'bitrix24', 'ognemet', 'quickley', 'venyoo', 'carrotquest', 'onicon', 'streamwood', 'zendesk', 'cackle', 'comagic', 'livechat', 'cloudim', 'wazzup24', 'sales-helper', 'ssd.tools', 'smsint', 'freshoffice', 'bothelp', 'salesforce', 'olark', 'kayako', 'useresponse', 'callbackhunter', 'fstrk', 'umnico', 'helpcrunch', 'chaport', 'mesj', 'me-talk', 'pozvonim', 'mssg', 'chat2desk', 'callpy', 'sms-uslugi', 'yamichat', 'liveagent', 'mcn.ru', 'chatim', 'calltouch', 'telegramhelper', 'tawk', 'rocket.chat', 'wix', 'webisonline', 'uiscom', 'webway', 'crafttalk', 'pfka', 'suppchat', 'gorgias', 'tidio', 'purechat', 'revechat', 'podium', 'socialintents', 'hubspot', 'elfsight', 'chatbot', 'kwizbot', 'acquire', 'widget__social', '3cx', 'userlike', 'helpscout', 'board.support', 'formilla', 'liveperson', 'telegram-feedback', 'pact.im', 'talkdriver', 'i2crm', 'angry.space', 'bachata', 'flomni', 'edna', 'usedesk', 'chatapp', 'pachca', 'yeahdesk', 'chat-center', 'blinger', 'allinone', 'roistat', 'callbaska', 'online-consultant', 'leadback', 'salebot', 'konveier', 'talker24', 'callshark', 'amocrm', 'amo.tm', 'imbachat', 's-chat', 'tocha', 'prodalet', 'okocrm', 'beeper', 'samosale', 'retailcrm']
dba = [] # сюда добавляются словари с найденными и не найденными чатами/телеграмами
tmp_for_urls_complete_txt = [] # тут хранятся временные сделанные для последующего переноса в файл all_urls_complete.txt и с найденными и с нейнайденными чатами/телеграмами
super_tmp_all_urls = [] # тут хранятся временные выгруженные из all_urls_complete.txt, чтобы по ним не проходить, + добавляются новые для осетивания дублей
count2_1 = 0
count2_2 = 1
count2_3 = 2
count2_4 = 3
count3 = 0
count4 = 0
ss = 1
# открываем главный json
with open('cities/Novokuznetsk/save.json', 'r', encoding='utf8') as f:
    data = json.load(f)
# выгружаю из файла урлы в переменную super_tmp_all_urls для проверки через not in
with open('all_urls_complete.txt', 'r', encoding='utf8') as f:
    for e in f.readlines():
        super_tmp_all_urls.append(e.lower().strip().replace('https:', '').replace('http:', '').replace('/', '').replace('www.', ''))
# главный цикл по обработке файла
name = ''
phone1 = ''
phone2 = ''
phone3 = ''
phone4 = ''
# проход по циклу
s = len(data['features'])
for i in data['features']:
    # в переменные передаем данные компании текущего цикла
    try:
        name = i['properties']['CompanyMetaData']['name']
        url = i['properties']['CompanyMetaData']['url']
        url = url.lower().strip().replace('https:', '').replace('http:', '').replace('/', '').replace('www.', '')
        phone1 = i['properties']['CompanyMetaData']['Phones'][count2_1]['formatted']
        phone2 = i['properties']['CompanyMetaData']['Phones'][count2_2]['formatted']
        phone3 = i['properties']['CompanyMetaData']['Phones'][count2_3]['formatted']
        phone4 = i['properties']['CompanyMetaData']['Phones'][count2_4]['formatted']
    except:
        ...
    if url not in super_tmp_all_urls:
        tmp_for_urls_complete_txt.append(url)
        # добавляем во временный словарь db эти данные текущего цикла
        if url not in super_tmp_all_urls:
            try:
                q = requests.get(f'http://{url}'.strip())
            except:
                ...
            print('url —', f'http://{url}')
            try:
                q = q.text
            except:
                ...
            # парсинг телеграм
            b = q.find('t.me')
            b1 = q[b:]
            b2 = b1.find('"')
            c = q.find('telegram.me')
            c1 = q[c:]
            c2 = c1.find('"')
            # добавление найденного в переменные
            tg1 = b1[:b2].replace('t.me/', 'tg://resolve?domain=').strip()
            tg2 = c1[:c2].replace('telegram.me/', 'tg://resolve?domain=').strip()
            tg1 = tg1[:-1]
            tg2 = tg2[:-1]
            if len(tg1) > len(tg2):
                print('tg1 —', tg1)
            else:
                print('tg2 —', tg2)
            # определение сайтов с чатами
            for i in chats:
                chat = ''
                for i in chats:
                    a = q.find(i)
                    if a > 0:
                        chat += i
                        break
            print('chat —', chat)
            # парсинг вацапов v1
            h = q.find('api.whatsapp')
            h1 = q[h:]
            hm = 0
            h2 = h1.find('"')
            h2_1 = h1.find("'")
            if len(h1[:h2]) > hm:
                wa = h1[:h2]
                hm = len(h1[:h2])
                if len(h1[:h2_1]) < hm:
                    wa = h1[:h2_1]
                print('wa —', wa)
            # парсинг вацапов v2
            h = q.find('wa.me')
            h1 = q[h:]
            hm = 0
            h2 = h1.find('"')
            h2_1 = h1.find("'")
            if len(h1[:h2]) > hm:
                wa = h1[:h2]
                hm = len(h1[:h2])
                if len(h1[:h2_1]) < hm:
                    wa = h1[:h2_1]
                print('wa —', wa)
            # парсинг vk
            h = q.find('href="https://vk.com')
            hh1 = q[h:]
            hh = hh1.find('vk.com')
            h1 = hh1[hh:]
            hm = 0
            h2 = h1.find('"')
            h2_1 = h1.find("'")
            if len(h1[:h2]) > hm:
                vk = h1[:h2]
                hm = len(h1[:h2])
                if len(h1[:h2_1]) < hm:
                    vk = h1[:h2_1]
                print('vk —', vk)
            # парсинг email
            u = '@' + url
            aa = [u, '@rambler.ru', '@yandex.ru', '@mail.ru', '@list.ru', '@bk.ru', '@gmail.com', '@ya.ru',
                  '@outlook.com']
            bb = aa[1] in q
            for i in aa:
                if i in q:
                    a0 = i
                    break
                else:
                    a0 = ''
            a11 = len(a0)
            a1 = q.find(a0)
            a2 = q[a1 - 20:]
            a3 = a2.find(a0)
            a4 = a2[:a3 + a11]
            a5 = a4[::-1]
            a6_1 = a5.find(' ')
            a6_2 = a5.find(':')
            a6_3 = a5.find('>')
            a7_1 = a5[:a6_1]
            a7_2 = a5[:a6_1]
            a7_3 = a5[:a6_3]
            a8_1 = a7_1[::-1]
            a8_2 = a7_2[::-1]
            a8_3 = a7_3[::-1]
            a9_1 = len(a8_1)
            a9_2 = len(a8_2)
            a9_3 = len(a8_3)
            if a9_1 < a9_2 or a9_1 < a9_3:
                aaa = a8_1.replace('\t', '').replace('\n', '')
            elif a9_2 < a9_1 or a9_2 < a9_3:
                aaa = a8_2.replace('\t', '').replace('\n', '')
            else:
                aaa = a8_3.strip().replace('\t', '').replace('\n', '')
            try:
                eee = aaa.find(':')
                email = aaa[eee+1:]
                print('email —', email)
            except:
                ...
            # добавление в бд спарсенного
            try:
                new = {}
                new.update({'name': name, 'url': url, 'phone1': phone1})
                try:
                    new.update({'phone2': phone2})
                except:
                    ...
                try:
                    new.update({'phone3': phone3})
                except:
                    ...
                try:
                    new.update({'phone4': phone4})
                except:
                    ...
                try:
                    new.update({'tg': tg1})
                except:
                    ...
                try:
                    new.update({'tg2': tg2})
                except:
                    ...
                try:
                    new.update({'chat': chat})
                except:
                    ...
                try:
                    new.update({'vk': vk})
                except:
                    ...
                try:
                    new.update({'wa': wa})
                except:
                    ...
                try:
                    new.update({'email': email})
                except:
                    ...
            except:
                ...
            dba.append(new)
            name = ''
            url = ''
            phone1 = ''
            phone2 = ''
            phone3 = ''
            phone4 = ''
            vk = ''
            wa = ''
            email = ''
    super_tmp_all_urls.append(url)
    print(f' ————————————————————————————————— прошли {ss} из {s} —————————————————————————————————')
    ss += 1
# заносим новые юрлы в файл, чтобы потом по ним не повторять прохооды
with open('all_urls_complete.txt', 'a', encoding='utf8') as f3:
    for i in tmp_for_urls_complete_txt:
        f3.write(i)
        f3.write('\n')
# отображаем итоговый список для копирования в google sheets
try:
    for i in dba:
        print(i['name'], i['url'])
except:
    ...
