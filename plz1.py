import requests
import json
import time
import csv
import sys
import csv
 
f = open('data1.csv','r')
rdr = csv.reader(f)
datalist=[]
for line in rdr:
    datalist=line
    
f.close()
category={'3d-printer-accessories': '3D Printing', '3d-printer-extruders': '3D Printing', '3d-printer-parts': '3D Printing', '3d-printers': '3D Printing', '3d-printing-tests': '3D Printing', 'coins-and-badges': 'Art', 'interactive-art': 'Art', 'math-art': 'Art', 'scans-and-replicas': 'Art', 'sculptures': 'Art', 'signs-and-logos': 'Art', 'accessories': 'Fashion', 'bracelets': 'Fashion', 'costume': 'Fashion', 'earrings': 'Fashion', 'glasses': 'Fashion', 'jewelry': 'Fashion', 'keychains': 'Fashion', 'rings': 'Fashion', 'audio': 'Gadgets', 'camera': 'Gadgets', 'computer': 'Gadgets', 'mobile-phone': 'Gadgets', 'tablet': 'Gadgets', 'video-games': 'Gadgets', 'automotive': 'Hobby', 'diy': 'Hobby', 'electronics': 'Hobby', 'music': 'Hobby', 'rc-vehicles': 'Hobby', 'robotics': 'Hobby', 'sport-and-outdoors': 'Hobby', 'bathroom': 'Household', 'containers': 'Household', 'decor': 'Household', 'household': 'Household', 'supplies': 'Household', 'kitchen-and-dining': 'Household', 'office-organization': 'Household', 'outdoors-and-garden': 'Household', 'pets': 'Household', 'biology': 'Learning', 'engineering': 'Learning', 'math': 'Learning', 'physics-and-astronomy': 'Learning', 'animals': 'Models', 'building-and-structures': 'Models', 'creatures': 'Models', 'food-and-drinks': 'Models', 'model-furniture': 'Models', 'model-robots': 'Models', 'people': 'Models', 'props': 'Models', 'vehicles': 'Models', 'hand-tools': 'Tools', 'machine-tools': 'Tools', 'tool-holders-and-boxes': 'Tools', 'chess': 'Toys & Games', 'construction-toys': 'Toys & Games', 'dice': 'Toys & Games', 'games': 'Toys & Games', 'mechanical-toys': 'Toys & Games', 'playsets': 'Toys & Games', 'puzzles': 'Toys & Games', 'toy-and-game-accessories': 'Toys & Games'}
f = open('modelData1.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(['id','name','thumbnail',"added","likeCount","collectCount","commentCount","description","instruction","tags","fileCount","downloadCount","viewCount","remixCount","makeCount","rootCommentCount","bigCategory","smallCategory","comments"])



cnt=0
for i in datalist:
    print(i,int(i))
    cnt+=1
    url="https://api.thingiverse.com/things/"+str(int(i))+"?access_token=009771366fb227909df098e04303677c"
    print(url)
    response = requests.get("https://api.thingiverse.com/things/"+i+"?access_token=009771366fb227909df098e04303677c")
    data=response.json()
    
    try:
        #print(data['creator'])
        params={}
        params["id"]=data["id"]

        params["name"]=data["name"]

        

        # params["createrName"]=data["creator"]["name"]


        params["added"]=data["added"][:10]
        
        params["thumbnail"]=data["thumbnail"]


        params["likeCount"]=data["like_count"]

        params["collectCount"]=data["collect_count"]

        params["commentCount"]=data["comment_count"]

        params["description"]=data["description"]
        params["instruction"]=data["instructions"]

        #instruction
        taglist=[]
        for tag in data["tags"]:
            taglist.append(tag["tag"])
        params["tags"]=taglist

        params["fileCount"]=data["file_count"]

        params["downloadCount"]=data["download_count"]
        params["viewCount"]=data["view_count"]
        params["remixCount"]=data["remix_count"]

        params["makeCount"]=data["make_count"]
        params["rootCommentCount"]=data["root_comment_count"]
        
        params["createrName"]=data["creator"]["name"]
        params["firstName"]=data["creator"]["first_name"]
        params["lastname"]=data["creator"]["last_name"]
        params["modelThumbnail"]=data["creator"]["thumbnail"]
        params["countOfFollwers"]=data["creator"]["count_of_followers"]
        params["countOfFollwings"]=data["creator"]["count_of_following"]
        params["countOfDesigns"]=data["creator"]["count_of_designs"]
        params["location"]=data["creator"]["location"]

        
        
        response = requests.get("https://api.thingiverse.com/things/"+str(i)+"/categories?access_token=009771366fb227909df098e04303677c")
        data=response.json()
        params["slug"]=data[0]["slug"]
        params["bigCategory"]=category[data[0]["slug"]]
        
        # params["slug"]="slug"
        # params["bigCategory"]="slug"
        #35.73.182.58
        URL="http://35.73.182.58:8080/data/makedata"
        headers = {'Content-Type': 'application/json; charset=utf-8'}

        res=requests.post(URL,headers=headers,data=json.dumps(params))

        url="https://api.thingiverse.com/things/"+str(i)+"/threaded-comments/?access_token=009771366fb227909df098e04303677c"
        response = requests.get(url)
        data=response.json()
        comments=""
        for commentList in data["comments"]:
            for comment in data["comments"][commentList]:
                comments+=comment["body"]
                
        
        
        wr.writerow([params['id'], params['name'],params['thumbnail'],params["added"],params["likeCount"],params["collectCount"],params["commentCount"],params["description"],params["instruction"],params["tags"],params["fileCount"],params["downloadCount"],params["viewCount"],params["remixCount"],params["makeCount"],params["rootCommentCount"],params["bigCategory"],params["slug"],comments])

        print(i,"success",cnt)
        
    except Exception as e:
        print(i,"fail",e)
        
f.close()


'''
3D Printing:3d-printer-accessories
3D Printing:3d-printer-extruders
3D Printing:3d-printer-parts
3D Printing:3d-printers
3D Printing:3d-printing-tests
Art:coins-and-badges
Art:interactive-art
Art:math-art
Art:scans-and-replicas
Art:sculptures
Art:signs-and-logos
Fashion:accessories
Fashion:bracelets
Fashion:costume
Fashion:earrings
Fashion:glasses
Fashion:jewelry
Fashion:keychains
Fashion:rings
Gadgets:audio
Gadgets:camera
Gadgets:computer
Gadgets:mobile-phone
Gadgets:tablet
Gadgets:video-games
Hobby:automotive
Hobby:diy
Hobby:electronics
Hobby:music
Hobby:rc-vehicles
Hobby:robotics
Hobby:sport-and-outdoors
Household:bathroom
Household:containers
Household:decor
Household:household
Household:supplies
Household:kitchen-and-dining
Household:office-organization
Household:outdoors-and-garden
Household:pets
Learning:biology
Learning:engineering
Learning:math
Learning:physics-and-astronomy
Models:animals
Models:building-and-structures
Models:creatures
Models:food-and-drinks
Models:model-furniture
Models:model-robots
Models:people
Models:props
Models:vehicles
Tools:hand-tools
Tools:machine-tools
Tools:tool-holders-and-boxes
Toys & Games:chess
Toys & Games:construction-toys
Toys & Games:dice
Toys & Games:games
Toys & Games:mechanical-toys
Toys & Games:playsets
Toys & Games:puzzles
Toys & Games:toy-and-game-accessories
'''