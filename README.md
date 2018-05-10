# Web_scrapping
web_scrapping_using_python
Example 1:
# NPTL DOWNLOADER
------------------
Need for this web_scrapping:
    
        while downloading the lecture videos from NPTL sities, I found out, we have to manually doanload each video.
    Also some of the Downloaded videos are not in proper order. Even if we retrieve from the youtube playlist 
    most of the playlist are suffled.Hence, its hard to properly download the videos. 
        Since most of the donwloder (like bitcomet, IDM and so on) comes with the option of batch download.
    (i.e we have to provide the url, then these downloader will download all the videos for us).
        Just for the own statisfication, i wrote a program, which will fetch the videos and save the links in 
    both .csv and .txt file.
   
   Features using my NPTL downloader:
      
      1) we can fetch and download the video as per own convienent format such as 
         mp4,3gp and Flv format(All available format from NPTL).
      2) Ease of Use.
      3) Links are easily sharable.
    
   How to Run the script(Download the videos)
   
    Method 1: Flexible Way 
    =========================
      1) Download the "Nptl_Downloader.py" file from this repo.
      
      2) necessary packages
          i) request
                if dont have it install by "pip install request"
          ii) BeautifulSoup 
                if dont have it install by "pip install beautifulsoup4"

      3) Run by using python 3 or above versions.
      
      4) after running the file  
          ---> provide the url of full download page.
                  This kind of page url: http://nptel.ac.in/courses/nptel_download.php?subjectid=117106113 
          ---> provide the formate u want to download
                  use    mp4 (or) 3gp (or) flv     (Note: case sensitive)
          ---> provide the file name of your wish to save the video urls.
          
          Thats it now, urls are ready in csv as well as in text file format.
          
       5) Download via Downloader: Use bitcomet
          just give the text file to the bitcomet it will download all the videos from the given course url.
      
      Method 2: Hard Way via argparser
      =================================
      1) Download the "Nptl_Downloader_using_argparse.py" file from this repo.
      
      2) necessary packages
          i) request
                if dont have it install by "pip install request"
          ii) BeautifulSoup 
                if dont have it install by "pip install beautifulsoup4"
                
      3) In terminal Run the code, give all the below details using argparse way in terminal.  
          ---> provide the url of full download page.
                  This kind of page url: http://nptel.ac.in/courses/nptel_download.php?subjectid=117106113 
          ---> provide the formate u want to download
                  use    mp4 (or) 3gp (or) flv     (Note: case sensitive)
          ---> provide the file name of your wish to save the video urls.
            
            Example usage  in terminal:   
            ---------------------------
               "python NPTL_Downloader_using_argparse.py --url http://nptel.ac.in/courses/nptel_download.php?subjectid=117106113       
               --format 3gp  --csv_filename course1"
               
          Thats it now, urls are ready in csv as well as in text file format.
          
       5) Download via Downloader: Use bitcomet
          just give the text file to the bitcomet it will download all the videos from the given course url.
          
 
    For queries and doubts mail me. (link in profile)
