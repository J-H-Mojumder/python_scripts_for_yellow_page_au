# Python script using selenium webDriver to scrape Yellow Pages of Australia.

I have used **selenium webdriver, xlsxwriter and time** library of Python. I have used **geckodriver** as the driver. One just have to change the URL in the 9th line of the script and replace with his or her destination page. After the browser opens there will be a captcha if someone want to access the website from outside Australia. This captcha needs to be solved manually and for this I have delayed the program for 20 seconds for the first page only. People from Australia can omit the
''' python
    if count == 0:
        time.sleep(20)
'''
part. It will create an excel file and name it as "yellow_pages_"+category_name+"_"+state_name+".xlsx" and will grab columns 'Business Name', 'Address', 'Website URL', 'Phone', 'Email', 'category', 'State'.
