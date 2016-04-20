import NahabinoParser
import re
import urllib
import datetime

r = urllib.urlopen('http://krasnogorsk.cian.ru/snyat-2-komnatnuyu-kvartiru-moskovskaya-oblast-krasnogorskiy-rayon-nahabino-01197900/')
#r = urllib.urlopen('http://www.cian.ru/snyat-2-komnatnuyu-kvartiru-moskva-metro-molodezhnaya/')
#r = urllib.urlopen('http://krasnogorsk.cian.ru/snyat-2-komnatnuyu-kvartiru/')
#r = urllib.urlopen('http://www.cian.ru/snyat-2-komnatnuyu-kvartiru-moskva-metro-kantemirovskaya/')
#r = urllib.urlopen('http://krasnogorsk.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p=6&region=175071&room2=1&type=-2')
encoding = r.headers.getparam('charset')
s = r.read()
r.close()
p = NahabinoParser.NahabinoParser()
p.feed(s.decode(encoding))
result = re.findall(r'\d+ \d+', p.get_result())
list_coast = []
for str_uni in result:
    list_coast.append(float(str_uni.replace(u' ', u'')))
list_coast = sorted(list_coast)
num = len(list_coast)

print list_coast
print 'mediana = ', list_coast[len(list_coast)/2]
print 'average coast =', sum(list_coast)/float(num), num
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
f = open('coast_data.txt', 'a')
f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(num) + ',' + str(list_coast[len(list_coast)/2]) + ',' + '{0}'.format(sum(list_coast)/float(num)) + '\n\r')


