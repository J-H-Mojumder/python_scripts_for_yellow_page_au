import time
from selenium import webdriver
import xlsxwriter

driver = webdriver.Firefox(executable_path=r"E:\geckodriver.exe")
loop_counter = 1
count = 0
url = "https://www.yellowpages.com.au/search/listings?clue=motorcycle+shop&locationClue=Victoria&lat=&lon="
category_name = input("Enter category name : ")
state_name = input("Enter state name : ")

outputWorkbook = xlsxwriter.Workbook("yellow_pages_"+category_name+"_"+state_name+".xlsx")
outputsheet = outputWorkbook.add_worksheet()
outputsheet.write("A1", "Business Name")
outputsheet.write("B1", "Address")
outputsheet.write("C1", "Website URL")
outputsheet.write("D1", "Phone")
outputsheet.write("E1", "Email")
outputsheet.write("F1", "Category")
outputsheet.write("G1", "State")

row_counter = 1
while 1:
    driver.get(url)
    if count == 0:
        time.sleep(20)
    divs = driver.find_elements_by_class_name("listing-data")
    pagination = driver.find_elements_by_class_name("button-pagination-container")
    category = category_name
    state = state_name
    print("category : "+category)
    print("state : " + state)
    for div in divs:
        website_url = ""
        email_address = ""
        name = div.find_elements_by_class_name("listing-name")
        address = div.find_elements_by_class_name("listing-address")
        call_to_action = div.find_elements_by_class_name("call-to-action")
        contact = div.find_elements_by_class_name("contact-text")
        if len(call_to_action) >= 3:
            if call_to_action[1].text == "Send Email":
                email = call_to_action[1].find_elements_by_tag_name("a")
                email_address = email[0].get_attribute("data-email")
            elif call_to_action[2].text == "Send Email":
                email = call_to_action[2].find_elements_by_tag_name("a")
                email_address = email[0].get_attribute("data-email")
            if call_to_action[1].text == "Website":
                website = call_to_action[1].find_elements_by_tag_name("a")
                website_url = website[0].get_attribute("href")
            elif call_to_action[2].text == "Website":
                website = call_to_action[2].find_elements_by_tag_name("a")
                website_url = website[0].get_attribute("href")

        print("Business Name : "+name[0].text)
        if len(address) >= 1:
            print("Address : "+address[0].text)
        else:
            print("Address : ")
        print("Website URL : "+str(website_url))
        print("Phone : "+contact[0].text)
        print("Email : "+str(email_address))
        print("Category : "+category)
        print("State : "+state)

        outputsheet.write(row_counter, 0, name[0].text)
        if len(address) >= 1:
            outputsheet.write(row_counter, 1, address[0].text)
        else:
            outputsheet.write(row_counter, 1, "")
        outputsheet.write(row_counter, 2, str(website_url))
        outputsheet.write(row_counter, 3, contact[0].text)
        outputsheet.write(row_counter, 4, str(email_address))
        outputsheet.write(row_counter, 5, category)
        outputsheet.write(row_counter, 6, state)

        row_counter += 1
    if len(pagination) == 0:
        break
    else:
        page = pagination[0].find_elements_by_class_name("pagination")
    print(page[-1].text)
    if page[-1].text == "Next »":
        #page[-1].click()
        url = page[-1].get_attribute("href")
        count += 1
    else:
        break

outputWorkbook.close()