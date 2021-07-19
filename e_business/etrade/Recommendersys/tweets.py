import csv
import re

t_list = []
with open('bosuntweets101.csv', encoding='utf8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        t_list.append(row)

g_src = [t[0].lower() for t in t_list]  # fills in the list g_src with the names of tweeting users
g_tmp = [' ' + t[1] + ' ' for t in t_list]  # adds 1 space to beginning and end of each tweet
g_tmp = [t.split('@') for t in g_tmp]  # splits each tweet along @s
g_trg = [[t[:re.search('[^A-Za-z0-9_]', t).start()].lower().strip() for t in chunk] for chunk in
         g_tmp]

for line in g_trg:
    if len(line) > 1 and line[0] == '':  # removes blank entries from lines mentioning at least one name
        del line[0]

final = []
i = 0
for list in g_trg:  # creates final output list
    for name in list:
        final.append(g_src[i] + ',' + name + "\n")
    i += 1

with open('bosunload1.csv', mode='w') as out:
    for row in final:
        out.write(row)