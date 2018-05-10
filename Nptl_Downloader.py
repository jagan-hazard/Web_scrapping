"""
This is the web scrappin program to fetch the video url along with name for that video

Created on Wed May  9 20:05:49 2018

@author: Jagan
For queries and bugs: Please contact using below
e-mail: jagannathans92@gmail.com
github: https://github.com/jagan-hazard
instagram: https://www.instagram.com/jagan_is_blue/
"""
#%%
#To download the specific format (here MP4)
def mp4_format(formats,name_list,link_list):
    mp4_link=[]                                         #variable to store the video link
    name_link=[]                                        #variable to store the name
    for one in link_list:                               #loop through the links
        if '.mp4' in one:                               #find the specific formate to download here mp4
            a=link_list.index(one)                      #getting the mp4 link index from the list
            one1=one.replace(' ','%20')
            mp4_link.append(one1)                        #storing the mp4 links alone
            name_link.append(name_list[a])              #appending the names
    return (name_link,mp4_link)
#To download the specific format (here 3GP)
def threegp_format(formats,name_list,link_list):
    threegp_link=[]                                         #variable to store the video link
    name_link=[]                                        #variable to store the name
    for one in link_list:                               #loop through the links
        if '.3gp' in one:                               #find the specific formate to download here mp4
            a=link_list.index(one)                      #getting the mp4 link index from the list
            one1=one.replace(' ','%20')
            threegp_link.append(one1)                        #storing the mp4 links alone
            name_link.append(name_list[a])              #appending the names
    return (name_link,threegp_link)

#To download the specific format (here FLV)
def flv_format(formats,name_list,link_list):
    flv_link=[]                                         #variable to store the video link
    name_link=[]                                        #variable to store the name
    for one in link_list:                               #loop through the links
        if '.flv' in one:				                #find the specific formate to download here mp4
            a=link_list.index(one)                      #getting the mp4 link index from the list
            one1=one.replace(' ','%20')					
            flv_link.append(one1)                        #storing the mp4 links alone
            name_link.append(name_list[a])              #appending the names
    return (name_link,flv_link)

#writing it in a csv file
def writing_csv(filename,modified_variable):
    with open(filename,'w') as wf:
        for colm in modified_variable:
            wf.write(colm)
            wf.write('\n')
def writing_text(filename,modified_variable):
    with open(filename,'w') as wf:
        for colm in modified_variable:
            wf.write(colm)
            wf.write('\n')

#%%
#Getting the datas from web
def main():
	from bs4 import BeautifulSoup                                           #import beatifulsoup for web scrapping
	import requests                                                         #import requests for getting the html datas from any specific web link
	#import argparse                                                         #importing argparse to pass the parameters from the terminal
	running=True
	while running:
		x=int(input("""Nptl Downloader: @author:Jagannathan.S   \n
		Please enter your option:\n
		1.Download the material\n
		2.exit the program \n"""))
		if x==2:
			running=False
			return (running)
		elif x==1:
			if_url=input("Please paste your full video download url to download videos: ")
			if_format=input("Please enter the format you want to download(enter:mp4,3gp,flv): ")
			if_filename=input("Please enter the file name to save (without extension): ")
			source=requests.get(if_url).text #pass the weblink  
			soup=BeautifulSoup(source, 'lxml')                                                            #using beautifulsoup we get the necessay html datas
			main_table=soup.find('tbody')                                               #by inspecting the elements in website,we get to the necessary tag
			value=main_table.find_all('a')                      #find the all linked tags inside the 'tbody' tag
			name_list=[]                                        #to store the names of the video
			link_list=[]                                        #to store the link of the video
			for link in value:                                  #loop through all the seperate  links
				each=link["href"]								#just get the href link alone
				link_list.append(each)                          #append the link to the variable
				name=each.split("&")[2]                         #getting the file name (which is inside of the link itself)
				nam=name.split('=')[1]                          #getting specific and correct name
				name_list.append(nam)                           #append the name to the variable
			if if_format=='mp4':
				(name_link_new,mp4_link_new)=mp4_format(if_format,name_list,link_list)
			elif if_format=='3gp':
				(name_link_new,mp4_link_new)=threegp_format(if_format,name_list,link_list)				
			elif if_format=='flv':
				(name_link_new,mp4_link_new)=flv_format(if_format,name_list,link_list)
			else:
				print("Error:  Please enter the correct format")
				break
			#Inorder to store it in csv file, we need to some pre-processing the datas incertain format
			concatenated=[]                                    #converting the links and names in correct format
			for i in range(0,(len(name_list))//3):              #looping to the links
				conca=name_link_new[i]+','+mp4_link_new[i]      #changing into easy format
				concatenated.append(conca)
			csv_file_names=if_filename+'.csv'
			txt_file_names=if_filename+'_url.txt'       #append the results
			writing_csv(csv_file_names,concatenated)
			writing_csv(txt_file_names,mp4_link_new)
			print("""download completed \n
				Thank you""")
main()