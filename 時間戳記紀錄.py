import time
import os
filename = input('請輸入紀錄檔檔名 : ')



tagList = {}
cnt = 1
recordLog = []

while(1):
    text = input('請輸入初始化時間戳記類別，結束時請輸入-1 : ')
    if text == '-1':
        break
    tagList[cnt] = text
    cnt += 1
    
input('輸入任意值以開始記錄時間戳記...')
recordLog.append([time.localtime(), 0, '--開始--'])
ST_TIME = int(time.time())

while(1):
    os.system('cls')
    for line in recordLog:
        print(time.strftime("%Y-%m-%d %H:%M:%S", line[0]) + '\t' + str(line[1]) + '\t' + line[2])
    print('==========')
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
        recordLog.append([time.localtime(), diffTimeStr, tagList[int(tagNm)]])
    except:
        recordLog.append([time.localtime(), diffTimeStr, tagNm])
    os.system('cls')


    
c = input('是否校正紀錄起始時間點? Y/N : ')
while c.upper() == 'Y':
    stTime = input('請輸入影片開始時間 : ')
    for line in recordLog:
        deltaTime = int(time.mktime(line[0])) - int(time.mktime(time.strptime(stTime, "%Y-%m-%d %H:%M:%S")))
        if deltaTime < 0:
            line[1] = '##'
        else:
            line[1] = str(int(deltaTime/60)) + '\'' + str(deltaTime%60) + '\"'
    for line in recordLog:
        print(time.strftime("%Y-%m-%d %H:%M:%S", line[0]) + '\t' + str(line[1]) + '\t' + line[2])
    print('==========')
    ec = input('修正結果是否正確? Y/N : ')
    if ec.upper() == 'Y':
        break

print('紀錄開始寫入')
with open(filename + '.txt', 'a', encoding = 'utf8') as recordFile:
    for line in recordLog:
        recordFile.write(time.strftime("%Y-%m-%d %H:%M:%S", line[0]) + '\t' + str(line[1]) + '\t' + line[2] + '\n')
    recordFile.close()
    print('紀錄寫入完成')

with open(filename + '.txt', 'r', encoding = 'utf8') as recordFile:
    for line in recordFile:
        print(line, end= "")
    recordFile.close()
input('輸入任意值以離開程式...')
