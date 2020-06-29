from selenium import webdriver
import re
import sys
#Start selenium
browser = webdriver.Firefox()

tld=''
if(len(sys.argv) > 3):
    tld=' site:'+str(sys.argv[3])
#This function is for Google Dorking, or any Google Query with Selenium
def googleSearch(queries, output_mode,tld):
    result=[]
    #Run queries.
    if(output_mode == "-t"):
        for query in queries:
            print("Running query: "+query + tld)
            browser.get("https://www.google.com/search?q="+query+ tld)
            found_url_divs=browser.find_elements_by_class_name("r")
            found_description_divs=browser.find_elements_by_class_name("s")
            for url in found_url_divs:
                links=url.find_elements_by_tag_name("a")
                for link in links:
                    result.append(link.get_attribute("href"))
                for description in found_description_divs:
                    result.append(description.text)
    elif(output_mode == "-c"):
        for query in queries:
            print("Running query: " + query + tld)
            browser.get("https://google.com/search?q="+query + tld)
            found_divs=browser.find_elements_by_class_name("rc")
            for div in found_divs:
                result.append(div.text)
    else:
        print("Not a valid output mode. Output modes are -c and -t.")
    print("".join(result))
def googleDork(args):
    if(args[1] == "-fp"):
        queries=['intitle:"index of" application.ini','"admin password irreversible-cipher" ext:txt OR ext:log OR ext:cfg','intitle:"index of" "db.ini"','	"super password level 3 cipher" ext:txt OR ext:log','	intitle:"index of " "*.passwords.txt"','"MasterUserPassword" ext:cfg OR ext:log OR ext:txt -git','	"/etc/shadow root:$" ext:cfg OR ext:log OR ext:txt OR ext:sql -git','	inurl:*helpdesk* intext:"your default password is"','intitle:"index of" "passwords.xlsx"','	intitle:"index of" "config.neon" OR "config.local.neon"','intext:"Index of /password"','"config.php.bak" intitle:"index of"','"index of" ".env"','	filetype:env "DB_PASSWORD"','	"MYSQL_ROOT_PASSWORD:" ext:env OR ext:yml -git']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-av"):
        queries=['intext:Basato su IceWarp Server','inurl:wp-content/plugins/testimonial-rotator','	intitle:qdPM 9.1. Copyright (c) 2020 qdpm.net','intext:Basato su Comunicazioni Integrate IceWarp','	intext:"TopManage (R) 2002 - 2020"','inurl:wp-content/plugins/kingcomposer','	intext:powered by JoomSport - sport WordPress plugin','	inurl:wp-content/themes/newspaper','inurl:wp-content/plugins/elementor','"powered by Typo3"','"index of" "plugins/wp-rocket"','inurl:wp-content/plugins/brizy','index of /wp-content/uploads/backupbuddy','inurl:"wp-contentpluginsphoto-gallery"','inurl:wp-content/plugins/sportspress','inurl:wp-content/plugins/adrotate','inurl:wp-content/plugins/mappress-google-maps-for-wordpress','inurl:wp-content/plugins/yop-poll']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-ws"):
        queries=['-pub -pool intitle:"index of" "Served by" "Web Server"','intitle:"index of" "Served by Sun-ONE"','intitle:"Welcome to nginx!" intext:"Welcome to nginx on Debian!" intext:"Thank you for"','intitle:"Welcome to JBoss"','site:ftp.*.com "Web File Manager"','intitle:"Web Server\'s Default Page" intext:"hosting using Plesk" -www','intitle:"index of" "powered by apache " "port 80"','	"Powered by phpBB" inurl:"index.php?s" OR inurl:"index.php?style"','intext:"This is the default welcome page used to test the correct operation of the Apache2 server"','intitle:"index of" "debug.log" OR "debug-log"','intitle:"index of" "docker.yml"','inurl:":8088/cluster/apps"','"index of /private" -site:net -site:com -site:org','inurl:"id=*" & intext:"warning mysql_fetch_array()"','intext:"index of /" "Index of" access_log']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-vs"):
        queries=['intext:"Powered By Gila CMS"','intitle:"index of" "shell.php"','intitle:"index of" "filemail.pl"','inurl:/+CSCOE+/logon.html','intitle:"index of" "AT-admin.cgi"','intext:"(c) GUnet 2003-2007"','	"Powered by Jira Service Desk"','"Powered by vBulletin Version 5.5.4"','inurl:"q=user/password"','inurl:"/user/register" "Powered by Drupal" -CAPTCHA -"Access denied"','	inurl:"index.php?option=com_joomanager"','inurl:/proc/self/cwd','"dirLIST - PHP Directory Lister" "Banned files: php | php3 | php4 | php5 | htaccess | htpasswd | asp | aspx" "index of" ext:php','allintext:Copyright Smart PHP Poll. All Rights Reserved. -exploit','allinurl:moadmin.php -google -github','inurl:/elfinder/elfinder.html+intitle:"elFinder 2.0"','inurl:CHANGELOG.txt intext:drupal intext:"SA-CORE" -intext:7.32 -site:github.com -site:drupal.org','inurl:robots.txt intext:CHANGELOG.txt intext:disallow ext:txt -site:github.com','ext:cgi inurl:cgi-bin intext:#!/bin/bash']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-lp"):
        queries=['inurl:"index.php/user/password/" intext:Password Reset','inurl:candidatelogin.aspx','intext:"Welcome to Intranet" "login"','intext:"index of /" "customer.php" "~Login"','inurl:adminlogin.jsp','	index of "jira" inurl:login','"login" intitle:"intext:"Welcome to Member" login"','inurl:".Admin;-aspx }" "~Login"','intitle:"*Admin Intranet Login"','intitle:"index of" pass.php','inurl:.*org/login','intitle:"Intranet Login"','Pages Containing Login Portal into Various Web Server','	intitle:.*edu/login','inurl:employee-login.php','inurl:emplogin.aspx','inurl:"/index.php?route=account/forgotten"','inurl:resetpassword.do','inurl:admin/upload.asp','inurl:admin/login.aspx','inurl:admin/admin/Login','inurl:login.do?method=login','	inurl:userlogin.do','inurl:"passwordreset.asp"','intitle:adminlogin inurl:login','inurl:Cpanel/login.php','inurl:auth/Login','inurl:Cpanel/login.aspx','intitle:"index of" "admin-login.php"']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-fh"):
        queries=['inurl:"index of" wso','site:bamboo.*.* ext:action build','intitle:"(SSI Web Shell)" AND intext:"(ls -al)"','intitle:("Mini Shell") AND intext:("Upload File")','intitle:("Index of") AND intext:("c99.txt" OR "c100.txt")','inurl:"customer.aspx"','inurl:/servicedesk/customer/user/login','Find Microsoft Lync Server AutoDiscover','inurl:/download_file/ intext:"index of /"','intitle:"index of" "admin/xml"','inurl:logon/LogonPoint/index.html','inurl:"/arcgis/rest/services"','inurl:"/jmx-console/HtmlAdaptor?action','intitle:"index of" and intext:"vendor" and intext:"phpunit"']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-vo"):
        queries=['inurl:index.shtml','allinurl:top.htm?Currenttime','intitle:"HP ALM" "Application Lifecycle Management" inurl:/qcbin/ -ext:PDF','site:*/EWS/Exchange.asmx','inurl:/gmap.php?id=','inurl:/db.php?path_local=','intitle:"WeatherLinkIP Configuration"','	intitle:"Internet Services" inurl:default.htm intext:"FUJI XEROX"','intitle:"Kyocera Command Center" inurl:index.htm','inurl:/index.htm intext:"Oki Data Corporation"',"inurl:8080/dashboard.php","inurl:8080/dashboard intitle:Graphite Dashboard",'inurl:mainFrame.cgi intext:"RICOH"','	inurl:sws/index.html AND intext:"Model Name" AND intext:"Serial Number"','inurl:/?MAIN=DEVICE intitle:TopAccess intext:Device','inurl:/main.html intext:SHARP AND intext:MX-*','inurl:/dana-cached/sc/','inurl:/dana/home/ filetype:cgi','intitle:"index of" "cvsweb.cgi"','inurl:./sws/index.sws','inurl:SSI/index.htm','inurl:/frameprop.htm','inurl:"/English/pages_WinUS/" AND intitle:"Top page"','intitle:"Printer Status" AND inurl:"/PrinterStatus.html"']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-cam"):
        queries=['inurl:/live.htm intext:"M-JPEG"|"System Log"|"Camera-1"|"View Control"','intitle:NetworkCamera intext:"Pan / Tilt" inurl:ViewerFrame','inurl:"MultiCameraFrame?Mode=Motion"','intitle:"IP CAMERA Viewer" intext:"setting | Client setting"','intitle:"Device(" AND intext:"Network Camera" AND "language:" AND "Password"','inurl:control/camerainfo','allintitle: Axis 2.10 OR 2.12 OR 2.30 OR 2.31 OR 2.32 OR 2.33 OR 2.34 OR 2.40 OR 2.42 OR 2.43 "Network Camera"','(intitle:(EyeSpyFX|OptiCamFX) "go to camera")|(inurl:servlet/DetectBrowser)','	(intitle:MOBOTIX intitle:PDAS) | (intitle:MOBOTIX intitle:Seiten) | (inurl:/pda/index.html +camera)','	intitle:"WEBCAM 7 " -inurl:/admin.html','intitle:"webcamXP 5" inurl:8080 \'Live\'','inurl:/live.htm intext:"M-JPEG"|"System Log"|"Camera-1"|"View Control"','intitle:"NetcamSC IP Address"','intitle:"webcam 7" inurl:\'/gallery.html\'','intext:"Powered by www.yawcam.com"','	intitle:"Yawcam" inurl:8081','intitle:"webcamXP 5" -download','intext:"powered by webcamXP 5"','intitle:webcam 7 inurl:8080 -intext:8080']
        googleSearch(queries, args[2],tld)
    elif(args[1] == "-ji"):
        queries=['intitle:"index of" "id_rsa.pub"','Index of /__MACOSX/System','intext:"Not to be distributed" ext:doc OR ext:pdf OR ext:xls OR ext:xlsx','"Index of" "/access"','index of /backend/prod/config','"index of" "siri"','intext:"index of /" "*.yaml"','	intitle:"index of" secrets.yml','	intitle:"index of /" "*key.pem"','	intitle:"index of" admin.tar','index of .svn/text-base/index.php.svn-base','intext:"index of /" "config.json"','"index of sqlite"','intitle:index.of.?.db','	"Index of" "customer.php"']
        googleSearch(queries, args[2],tld)
    elif(args[1] =="-si"):
        queries=['intext:"Dumping data for table `orders`"','dcid= bn= pin code=','intext:"Powered by X-Cart: shopping cart software" -site:x-cart.com','intext:"powered by Hosting Controller" intitle:Hosting.Controller','site:ups.com intitle:"Ups Package tracking" intext:"1Z ### ### ## #### ### #"','inurl:shopdbtest.asp','"More Info about MetaCart Free"','inurl:midicart.mdb','inurl:"shopadmin.asp" "Shop Administrators only"','POWERED BY HIT JAMMER 1.0!','inurl:"/database/comersus.mdb"']
        googleSearch(queries,args[2],tld)
    elif(args[1] == "-help"):
        print("General Usage: python dorkscraper.py <dork> <output_mode> <tld>")
        print("Dorks:")
        print("-fp for password files. <dork>")
        print("-av for advisories and vulnerabilities. <dork>")
        print("-ws for web servers. <dork>")
        print("-vs for vulnerable servers. <dork>")
        print("-lp for login portals. <dork>")
        print("-fh for footholds. <dork>")
        print("-vo for various online devices <dork>")
        print("-cam for online cameras. <dork>")
        print("-ji for juicy information <dork>")
        print("-si for sensitive shopping info. <dork>")
        print("Output Modes")
        print("-t will output total information, in an unclean format. URLS and descriptions. <output_mode>")
        print("<output_mode> -c will output some information in a clean format, the URLS will be formated something like this:")
        print("url.com > route > file >etc > ext >PDF")
        print("The > means / or . : url.com/route/file/etc/ext.pdf")
        print("Top Level Domain")
        print("<tld> is for the top level domain or target site you're google dorking. Example: target.com or .gov")
    else:
        print("Unknown argument, use dorkscraper.py -help for help.")
    #Get links and Descriptions
    #Turn them into strings for parsing.
    #Return results.
googleDork(sys.argv)
browser.quit()
