from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import maskpass
import pyfiglet

result = pyfiglet.figlet_format("Cookie Monster", font = "slant"  )
print(result)
print('''
    ---------------------------------------------------------------------------------------------------------------                                                   
    RedHawks Cyber Research | DL28 (NavidNaf)
    ---------------------------------------------------------------------------------------------------------------   
''')

driver = webdriver.Firefox(executable_path="") #Add path to your local driver
website = input("Enter Website (full URL):")
user1 = input("Enter Username: ")
password1 = maskpass.askpass(prompt="Enter Password: ", mask="#")

driver.get(website)
print(driver.title)
emailAddr = driver.find_element(By.ID, "email") #Change Here
print("Entering Email")
emailAddr.send_keys(user1)
sleep(3)
passwd = driver.find_element(By.ID, "password") #Change Here
print("Entering Password")
passwd.send_keys(password1)
sleep(3)
login = driver.find_element(By.TAG_NAME, "button") #Change Here
print("Logging In")
login.click()

sleep(5)
#Cookie Grabbing
driver.execute_script('''localStorage.removeItem("user");''') #Change Here
print("Cookie Removed")
sleep(1)
driver.execute_script('''
                            # Desired Changed Local Storage value.
                            # localStorage.setItem("user","")

                            ''')
print("Cookie Altered")
sleep(1)
print(driver.execute_script('''return localStorage.getItem('user');''')) #Change Here
sleep(5)
print("Attempting Reload")
driver.execute_script("location.reload()")
print("Success")