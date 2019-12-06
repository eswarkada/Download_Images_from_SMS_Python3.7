#eswarkada

import urllib.request
import requests
id1 = input("enter the id: ")
id2 = input("enter last id: ")

r= requests.session()

#N169999.jpg"

for i in range(int(id1),int(id2)):
    image = "N"+str(i)+".jpg"
    url="http://intranet.rguktn.ac.in/SMS/usrphotos/user/"+image
    i1 = r.get(url)
    if(i1.status_code==200):
        print("N"+str(i)+" image found!!!")
        urllib.request.urlretrieve(url,image)
    else:
        print("N"+str(i)+" image not found.......")
    
