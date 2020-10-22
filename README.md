# Python script using selenium webDriver to scrape Yellow Pages of Australia.

I have used **selenium webdriver, xlsxwriter and time** library of Python. I have used **geckodriver** as the driver. One have to add his/her geckodriver location in the below mentioned line.
```python
driver = webdriver.Firefox(executable_path=r"E:\geckodriver.exe")
```

One just have to change the URL in the 8th line of the script and replace with his or her destination page.

```python
url = "https://www.yellowpages.com.au/search/listings?clue=motorcycle+shop&locationClue=Victoria&lat=&lon="
```

After the browser opens there will be a captcha if someone want to access the website from outside Australia. This captcha needs to be solved manually and for this I have delayed the program for 20 seconds for the first page only. People from Australia can omit the below mentioned part.

``` python
    if count == 0:
        time.sleep(20)
```

It will create an excel file and name it as "yellow_pages_"+category_name+"_"+state_name+".xlsx". You can change the naming format of the excel file in the below mentioned line.

```python
outputWorkbook = xlsxwriter.Workbook("yellow_pages_"+category_name+"_"+state_name+".xlsx")
```

It will grab columns 'Business Name', 'Address', 'Website URL', 'Phone', 'Email', 'category', 'State'. You can change the placement of the columns by changing in the below mentioned part.

```python
outputsheet.write("A1", "Business Name")
outputsheet.write("B1", "Address")
outputsheet.write("C1", "Website URL")
outputsheet.write("D1", "Phone")
outputsheet.write("E1", "Email")
outputsheet.write("F1", "Category")
outputsheet.write("G1", "State")
```
