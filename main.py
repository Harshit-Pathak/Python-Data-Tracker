import requests
import bs4
import tkinter as tk
def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_detail_of_india():
    url="https://www.mohfw.gov.in/"
    html_data=get_html_data(url)
    print(html_data.text)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    print(bs.prettify())
    info_div = bs.find("div",class_="site-stats-count").find("ul").findAll("li")
    all_detail = ""
    for item in info_div[0:4]:
        count = item.find("strong").get_text()
        text = item.find("span").get_text()
        all_detail = all_detail + text + " : " + count + "\n"
    return all_detail

#refresh function to update the status
def refresh():
    newdata=get_corona_detail_of_india()
    print('Refreshing...')
    mainLabel['text'] = newdata


#creating gui
root=tk.Tk()
root.geometry("700x450")
root.title("COVID 19 DATA TRACKER - INDIA")
root.configure(background='orange')
f=('calibri',20,'bold')

banner = tk.PhotoImage(file="download.pgm")
bannerLabel = tk.Label(root,image=banner)
bannerLabel.pack()

mainLabel=tk.Label(root,text=get_corona_detail_of_india(),font=f,bg='orange')
mainLabel.pack()

rebtn=tk.Button(root,text='REFRESH',font=f,relief='solid',command=refresh)
rebtn.pack()


root.mainloop()
