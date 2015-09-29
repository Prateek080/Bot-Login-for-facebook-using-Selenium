import urllib2,urllib, cookielib, re, os, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from selenium import webdriver
import time
import sys
import random
from bs4 import BeautifulSoup

#all the packages imports neccesary for running the software
class Facebook:

    def login(self,email,password):
            '''
            function name: login
            discription:It accepts email and passwords from the main file in the class and login it into the facebook
            :param email:
            :param password:
            :returns:void
            '''
            
            driver = webdriver.Firefox()
            driver.get("https://facebook.com")
              

            login="loginbutton"
            emailelement = driver.find_element_by_name("email")
            passwordelement = driver.find_element_by_name("pass")
            emailelement.send_keys(email)
            passwordelement.send_keys(password)
            loginelement = driver.find_element_by_id(login)
            loginelement.click()
            time.sleep(5)
            url=driver.current_url
            print url
            #this if will run only if password and email combo is wrong
            if(url=="https://www.facebook.com/login.php?login_attempt=1&lwv=110"):
                        print "Login failed."
                        driver.close()


            else:
                        soup = BeautifulSoup(driver.page_source)
                        mydivs = soup.find("div", { "class" : "_8u _42ef" }).find('a')
                        print mydivs.text
                        local_name=""+mydivs.text+str(random.randint(0,100))+".jpg"
                        raw_src = soup.find("div", { "class" : "_mp3 _38vo" }).find('img')
                        url=raw_src.get('src')
                        urllib.urlretrieve(url, local_name)
                        print "Image Saved Successfully"

                        time.sleep(2)
                        driver.close()
                        

                        

                        


    def inp(self):
            """
            function name:inp
            function discription:It accepts the username and passwords from the terminal and sends it to the login
                                function
            :return:void
            """
            #input the Email Id
            email=raw_input("Email Id: ")
            #input the password
            password=getpass.getpass("Password: ")
            #if the password is empty then it will ask for one more time.
            if password=="":
                password=getpass.getpass("Password is Blank.ReEnter Password: ")


            call_2 = Facebook()
            call_2.login(email,password)


if __name__ == '__main__':
    
            start = Facebook()
            start.inp()







