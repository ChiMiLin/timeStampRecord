import time
import os
filename = input('請輸入紀錄檔檔名 : ')

recordFile = open(filename + '.txt', 'a', encoding = 'utf8')

# recordFile.writeline

tagList = {}
cnt = 1

while(1):
    text = input('請輸入初始化時間戳記類別，結束時請輸入-1 : ')
    if text == '-1':
        break
    tagList[cnt] = text
    cnt += 1
    
input('輸入任意值以開始記錄時間戳記...')
recordFile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' --開始--\n')
ST_TIME = int(time.time())

while(1):
    os.system('cls')
    print('請輸入編號以標記時間戳')
    for i in tagList.keys():
        print(str(i) + ' : ' + tagList[i])
    print('-1 : 離開')
    tagNm = input(':')
    if tagNm == '-1':
        break
    
    diffTime = int(time.time()) - ST_TIME
    diffTimeStr = str(int(diffTime/60)) + '\'' + str(diffTime%60) + '\"'
    
    try:
        recordFile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\t' + diffTimeStr + '\t' + tagList[int(tagNm)] + '\n')
    except:
        recordFile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\t' + diffTimeStr + '\t' + tagNm + '\n')
recordFile.close()
os.system('cls')

with open(filename + '.txt', 'r', encoding = 'utf8') as recordFile:
    for line in recordFile:
        print(line.strip())
    recordFile.close()
input('輸入任意值以離開程式...')