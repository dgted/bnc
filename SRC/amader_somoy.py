

def Amader_Somoy(start_date, end_date, path, listbox_selected_category):
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

    #http://www.dainikamadershomoy.com/paper/more-news/2020 - 12 - 26
    base_address = "http://www.dainikamadershomoy.com/paper"

    all_url = []

    complete_url = base_address
    print(complete_url)

    # all_url.append([complete_url])
    cat_list = [
        "firstpage",
        "editorial",
        "khobor",
        "saradesh",
        "international",
        "sports",
        "entertainment",
        "lastpage",
        "money-time",
        "more-news"
    ]

    for d in All_date:
        for cat in cat_list:
            complete_url = base_address + '/' + cat + '/' + str(d)
            print(complete_url)
            all_url.append([complete_url])
            pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    #################################### 2222222222222222222222222222 #############################
    ######################################## 2nd part #############################################

    import bs4
    import requests
    import csv

    global all_unit_link, main_page_links

    all_unit_link = []
    main_page_links = []

    #base_address = "http://www.dainikamadershomoy.com/"
    #category = "archive/economy"

    def get_sub_links(main_page_link, path, listbox_selected_category):

        global all_unit_link

        #print(main_page_link)
        try:
            page = requests.get(main_page_link)
        except:
            print("error")
        p = int(page.status_code)
        while p != 200:
            print(page.status_code)
            page = requests.get(main_page_link)
            p = int(page.status_code)
        #print(page)

        try:
            soup = bs4.BeautifulSoup(page.content, 'html.parser')
        except:
            print("error")

        #print(soup)
        #print("--------------------------------------------------------------------------------")
        newsArticleDivs = soup.find_all("div", {"class": "w3-col m4"})

        for newsArticle in newsArticleDivs:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            # complete_url = base_address + news_link[0:]
            complete_url = news_link
            print(complete_url)
            for selected_cat in listbox_selected_category:
                selected_cat = str(selected_cat)
                if selected_cat in main_page_link:
                    for date in All_date:
                        date = str(date)
                        if date in main_page_link:
                            all_unit_link.append([complete_url, date, selected_cat])

        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='w',newline='') as unit_url_list:  ##########################################
            unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for url in list_to_be_inserted:
                # print(url)
                unit_url_writer.writerow(url)

        unit_url_list.close()

        pass

    with open(path+'/all_Archive_main_page_url.csv') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            main_page_links.append(row[0])

    print('+---------------------------------------------------------+')

    #get_sub_links(main_page_links[5])

    for main_link in main_page_links:
        try:
            get_sub_links(main_link, path, listbox_selected_category)
        except:
            pass
        pass

    write_csv(all_unit_link, path, listbox_selected_category)

    print(len(all_unit_link))

    ############################# 33333333333333333333333333333333333 ###########################
    ################################### 3rd part ################################################

    import bs4
    import requests
    import csv

    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    #CSV_LINK = 'amadershomoy_economy.csv'

    def append_to_csv(row, path, category):

        global CSV_LINK
        if category == 'All':
            CSV_LINK = path + "/Amader-Somoy_" + category + "_news.csv"
        else:
            CSV_LINK = path + "/Amader-Somoy_" + category + "_news.csv"

        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            news_article_writer.writerow(row)

        # news_article_writer.close()

        pass

    def get_title_and_content(url, news_date, news_cat, path, listbox_selected_category):
        BASE_URL = url
        page = requests.get(BASE_URL)
        # date = BASE_URL[42:52]

        soup = bs4.BeautifulSoup(page.content, 'html.parser')

        newsTitle = soup.find_all("h1")[0].getText()
        # print(newsTitle)
        article_text = soup.find("div", {"class": "w3-large img-am w3-justify"})

        all_paragraphs = article_text("p")

        news_content = ""

        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        # print(news_content)
        for cat in listbox_selected_category:
            cat = str(cat)
            if cat==news_cat:
                input_array = [news_date, newsTitle, news_content, news_cat]
                append_to_csv(input_array, path, news_cat)


        input_array = [news_date, newsTitle, news_content, news_cat]
        append_to_csv(input_array, path, 'All')

        pass

    with open(URL_LINK) as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            try:
                get_title_and_content(row[0], row[1], row[2], path, listbox_selected_category)
                print(i)
                i += 1
            except:
                print('exception occured')

