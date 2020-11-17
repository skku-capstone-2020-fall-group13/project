#-*- coding:utf-8 -*-
import urllib3
import json
import requests
import numpy as np

openApiURL = "http://api.vworld.kr/req/image" 

request="getmap"
service="image"
key = "2CCCA2EC-0108-3305-94F7-16446DB16433"
zoom="16"
size="1024,1024"
crs="EPSG:4326"
basemap="PHOTO"
layer="lt_c_uq111"
Param={"service":service,"request":request,"key":key,"zoom":zoom,"size":size,"basemap":basemap,"crs":crs}
file_idx=0
# Revise this parameters
## start point of target Area(left top of square)
start_center_x=126.97
start_center_y=37.28
## end point of target Area(right bottom of square)
end_center_x=127.0
end_center_y=37.33
## center movement
center_dif=0.01
#

center_x_list=np.arange(start_center_x,end_center_x,center_dif)
center_y_list=np.arange(start_center_y,end_center_y,center_dif)

for x in center_x_list:
    for y in center_y_list:
        # file name index (ex. Photo1, Photo2 ...)
        file_idx+=1
        # fix center parameter
        Param["center"]=str(x)+","+str(y)
        # GET
        response=requests.get(openApiURL,Param)
        # Check response status
        print("file num: ",file_idx)
        print("Status: ",response.status_code)
        file=open("Photo"+str(file_idx)+".png","wb")
        file.write(response.content)
        file.close()