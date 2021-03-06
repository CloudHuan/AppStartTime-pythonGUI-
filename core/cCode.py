#!_*_coding=utf-8_*_

import os,time,re,csv

class C_Tools():
    
    def isAdbEnabele(self):
        _shell = 'adb devices'
        _result = os.popen(_shell).readlines()
        if len(_result) >= 3:
            return True
        return False
    
    def startTimeLoop(self,pkgName,num,sign,mtext):
        
        _shell = 'adb shell am start -W %s'%pkgName
        _shell_stop = 'adb shell am force-stop %s'%pkgName.split('/')[0]
        time_list=[]
        for loop in range(int(num)):
            mtext.SetValue(u'第%s次执行'%(loop+1))
            os.popen(_shell_stop)
            
            if sign == True:
                self.clearApp(pkgName)
            startTime = os.popen(_shell).read()
            mResult = re.findall(u'TotalTime: (\d+)',startTime)[0]
            time_list.append(mResult)
            time.sleep(5)
        os.popen(_shell_stop)
        self.saveToCSV(time_list, pkgName, num,sign)
        mtext.SetValue(u'执行完毕')
        
    def saveToCSV(self,l_data,pkgName,num,sign):
        f = file('startTime.csv','a+')
        _writer = csv.writer(f)
        _writer.writerow([pkgName,'clean data?%s'%str(sign)])
        for item in l_data:
            _writer.writerow([item])
    
    def clearApp(self,pkgName):
        _shell_clear = 'adb shell pm clear %s'%pkgName.split('/')[0]
        os.popen(_shell_clear)
    
    def getCurrentActivity(self):
        _result = os.popen('adb shell dumpsys activity top|grep ACTIVITY').read().strip()
        return re.findall(u'ACTIVITY ([\w|.]+/[\w|.]+)',_result)[0]
    
    def writeConfig(self,mValue):
        with open('config.txt','w+') as f:
            f.write(mValue)
            print 'write config ok'
    
    def readConfig(self):
        with open('config.txt','r+') as f:
            print 'read config ok'
            return f.readline()