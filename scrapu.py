from bs4 import BeautifulSoup
import requests
r=requests.get("https://globalparents.contineo.in/index.php?option=com_studentdashboard&controller=studentdashboard&task=dashboard")
soup=BeautifulSoup(r.content,"html.parser")
div_text=soup.find("div",{"class":"coursename"})
print(div_text)



