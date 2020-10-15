import pandas as pd
import numpy as np
import uuid

from datetime import datetime

d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

df = pd.DataFrame(columns = ['SignUpId', 'CreditCard','Age','Gender','RegionCode','DeviceType','NoOfDevicesUsed','HoursPerDay','isPremiumserviceUsed','keyPress','NoShowsWatched','EoFEvents','EmptySearchResults','Wifi/MobileData','WatchSession','RecommendationSuccess','ExtenstionofTrails','GlobalEvent','DetectedMAC','ProfiledAge','WeekOfMonth','MostActiveTimeofDayForDataUsage','VPN','DownloadHistory','NoConnectedDevicesinHome','CostOfDevices','BoughtMembership'])
for i in range(10000):
    SignUpId = uuid.uuid1()
    CreditCard = np.random.randint(1,4) #VISA or MASTERCARD or Others
    Age = np.random.randint(13,99)
    Gender = np.random.randint(1,3) #MALE,FEMALE
    RegionCode = np.random.randint(1000,1010)
    DeviceType = np.random.randint(1,6) #Mobile,Tablet,TV,STB,OTHER
    NoOfDevicesUsed = np.random.randint(1,6)
    HoursPerDay = np.random.randint(1,20)
    isPremiumserviceUsed = np.random.randint(0,2)#No,Yes
    keyPress = np.random.randint(100,1000)
    NoShowsWatched = np.random.randint(1,10)
    EoFEvents = np.random.randint(1,10)
    EmptySearchResults = np.random.randint(1,5)
    Wifi_MobileData = np.random.randint(1,3)#wifi,Mobile
    WatchSession = np.random.randint(1,5)#morning,afternoon,evening,night
    RecommendationSuccess = np.random.randint(1,15) #numberof shows purchased from recomnedation lane
    ExtenstionofTrails = np.random.randint(0,5) #0:No
    GlobalEvent = np.random.randint(0,1) #withinonemonth
    DetectedMAC = uuid.uuid1() #UUID
    ProfiledAge = np.random.randint(0,3) #0:Teens 1:ADult 2:Senior Citizen
    WeekOfMonth = np.random.randint(1, 5)
    MostActiveTimeofDayForDataUsage = np.random.randint(1,5) #Morning,Afternoon,Evening,Night
    VPN = np.random.randint(0,2) #No or Yes
    DownloadHistory = np.random.randint(0,5) #Most active time for download #Morning,Afternoon,evening,night
    DownloadUsage = np.random.randint(1,2000) #1GB to 2000GB
    NoConnectedDevicesinHome = np.random.randint(1, 100) #list for all the devices connected
    CostOfDevices = np.random.randint(1000, 2000000) #cost of all connnected Devices
    BoughtMembership = np.random.randint(0,2) #0:No 1:Yes

    df.loc[i] = [SignUpId, CreditCard,Age,Gender,RegionCode,DeviceType,NoOfDevicesUsed,HoursPerDay,isPremiumserviceUsed,keyPress,NoShowsWatched,EoFEvents,EmptySearchResults,Wifi_MobileData,WatchSession,RecommendationSuccess,ExtenstionofTrails,GlobalEvent,DetectedMAC,ProfiledAge,WeekOfMonth,MostActiveTimeofDayForDataUsage,VPN,DownloadHistory,NoConnectedDevicesinHome,CostOfDevices,BoughtMembership]
df.to_csv('model.csv',index=False)
