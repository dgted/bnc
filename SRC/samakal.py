

def Samakal(start_date, end_date, path, listbox_selected_category):
    import bs4
    import requests
    import csv
    import pandas as pd
    from datetime import datetime

    print(start_date)
    print(end_date)
    print(path)
    print(listbox_selected_category)

    a = pd.date_range(start=start_date, end=end_date).to_pydatetime().tolist()
    All_date = []
    for i in a:
        d = str(i)
        #d = d.replace("-", '/')
        All_date.append(d[0:10])

    #https://samakal.com/archive?category=206&author=&tag=&date=2020-10-05&headline=
    # https://www.kalerkantho.com/print-edition/first-page/2020/12/01
    base_address = "https://samakal.com/archive?category="
    last_portion1 = "&author=&tag=&date="
    last_portion2 = "&headline="

    all_url = []

    complete_url = base_address
    print(complete_url)

    # all_url.append([complete_url])
    number_list = [
        "64",
        "65",
        "71",
        "67",
        "69",
        "70",
        "72",
        "104",
        "141",
        "153",
        "206"
    ]

    for d in All_date:
        for num in number_list:
            complete_url = base_address + num + last_portion1 + str(d) + last_portion2
            print(complete_url)
            all_url.append([complete_url])
            pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()


    ######################################### 2222222222222222222222222222 #############################
    ######################################## 2nd part ##################################################

    # creating two lists
    # main_page_links to extract from csv and store all main links
    global all_unit_link, main_page_links
    main_page_links = []
    # all_unit_link to store all sublinks
    all_unit_link = []

    with open(path+'/all_Archive_main_page_url.csv') as main_url_csv:
        readCSV = csv.reader(main_url_csv)
        for row in readCSV:
            main_page_links.append(row[0])

        # printing all main page links
        serial = 0
        for i in main_page_links:
            print(str(serial) + i)
            serial = serial + 1

    # to get all sub links from a main link
    def get_sub_links(main_page_link, path, listbox_selected_category):
        global all_unit_link
        page = requests.get(main_page_link)
        p = int(page.status_code)
        while p != 200:
            print(page.status_code)
            page = requests.get(main_page_link)
            p = int(page.status_code)
        # print(page)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        newsArticleDivs = soup.find_all("div", {"class": "news-content sm-100 xs-100 cpTMarginB"})
        article2 = soup.find_all("div", {"class": "news-content xs-100 cpItemMarginB"})
        article3 = soup.find_all("div", {"class": "media news-content child-cat-list"})
        article4 = soup.find_all("div", {"class": "col-md-7 col-sm-6 col-xs-12"})
        article5 = soup.find_all("div", {"class": "col-md-3 flex-col normalctg normalctgLead"})
        article6 = soup.find_all("div", {"class": "col-md-3 flex-col normalctg normalctgRight"})
        article7 = soup.find_all("div", {"class": "col-lg-6 col-md-6 col-sm-12 col-xs-12 fcategory-leadnews-cl"})
        article8 = soup.find_all("div", {"class": "col-lg-6 col-md-6 col-sm-6 col-xs-6"})
        article9 = soup.find_all("div", {"class": "col-lg-3 col-md-3 col-sm-6 col-xs-6"})

        for newsArticle in article7:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in article8:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in article9:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in article5:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in article6:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in article4:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in newsArticleDivs:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in article2:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        for newsArticle in article3:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            for cat in listbox_selected_category:
                cat = str(cat)
                if cat in complete_url:
                    all_unit_link.append([complete_url])

        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='w', newline='', encoding='utf-8') as unit_url_list:
            unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for url in list_to_be_inserted:
                print(url)
                unit_url_writer.writerow(url)
        unit_url_list.close()
        pass

    # checking of an individual link
    # get_sub_links(main_page_links[0])

    i = 1
    for main_link in main_page_links:
        if i <= 0:
            i += 1
            continue
        try:
            get_sub_links(main_link, path, listbox_selected_category)
        except:
            pass
        print(str(i) + " done !")
        i = i + 1
        pass
    print("All done")

    write_csv(all_unit_link, path, listbox_selected_category)

    print(len(all_unit_link))


    #################################### 33333333333333333333333333 ###################################
    #################################### 3rd part #####################################################

    def append_to_csv(row, path, category):
        global NEWS_CSV_LINK
        if category == 'All':
            CSV_LINK = path + "/Samakal_" + category + "_news.csv"
        else:
            CSV_LINK = path + "/Samakal_" + category + "_news.csv"

        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, path, listbox_selected_category):
        BASE_URL = url

        page = requests.get(BASE_URL)
        p = int(page.status_code)
        while p != 200:
            print(page.status_code)
            page = requests.get(BASE_URL)
            p = int(page.status_code)
        # print(type(page.status_code))

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        newsTitle = soup.find_all("title")[0].getText()
        # ----------------------------------------------Date and Writer--------------------------------------------------
        newsDate = soup.find("div", {"class": "col-md-4 col-md-offset-1 col-sm-12 col-xs-12"})
        newsDate = newsDate.find_all("span")[0].getText()
        newsDate = newsDate.strip()
        #print(newsDate)
        newsWriter = soup.find("div", {"class": "col-md-10 col-md-offset-1"})
        newsWriter = newsWriter.find_all("p")[0].getText()
        newsWriter = newsWriter.strip()
        #print(newsWriter)
        # ---------------------------------------------------------------------------------------------------------------
        #print(newsTitle)
        article_text = soup.find("div", {"class": "description"})
        # print(article_text)
        all_paragraphs = article_text("p")
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        if (news_content in ""):
            news_content = article_text.getText()
            news_content = news_content.replace("(adsbygoogle = window.adsbygoogle || []).push({});", "")
            news_content = news_content.strip()

        diff_line = news_content.splitlines()
        news_content = ""
        for line in diff_line:
            news_content += line

        #print("-----")
        #print(news_content[0:70])


        for category in listbox_selected_category:
            category = str(category)
            if category in url:
                All_cat = category
                input_array = [newsDate, newsTitle, news_content, category]
                append_to_csv(input_array, path, category)


        #cat = "bangladesh"

        #input_array = [newsTitle, news_content, TAG, newsDate, newsWriter]
        input_array = [newsDate, newsTitle, news_content, All_cat]
        append_to_csv(input_array, path, 'All')
        pass

    with open(path + '/all_Archive_unit_page_url.csv', encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            if i < 0:
                i += 1
                continue
            print(i)
            try:
                get_title_and_content(row[0], path, listbox_selected_category)
            except:
                pass
            i += 1
            pass
        print("All done")

