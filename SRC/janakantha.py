

def jana_kantha(start_date, end_date, path, listbox_selected_category):
    import bs4
    import requests
    import csv
    import pandas as pd
    from datetime import datetime

    print(start_date)
    print(end_date)
    print(path)
    print(listbox_selected_category)

    global all_category
    all_category = []

    a = pd.date_range(start=start_date, end=end_date).to_pydatetime().tolist()
    All_date = []
    for i in a:
        d = str(i)
        #d = d.replace("-", '/')
        All_date.append(d[0:10])

    #https://www.dailyjanakantha.com/print-media/2020-12-01/frontpage/

    base_address = "https://www.dailyjanakantha.com/print-media"

    all_url = []

    complete_url = base_address
    print(complete_url)
    cat_list = [
        "frontpage",
        "lastpage",
        "others",
        "national",
        "sports",
        "editorial",
        "quadruple",
        "trade",
        "international",
        "finance",
        "education",
        "reopinion",
        "politycs",
        "science",
        "bicitra",
        "cities",
        "toeditor",
        "city-election",
        "sports-feature",
        "glittering",
        "the-world",
        "ananda-kantha",
        "your-doctor",
        "economy",
        "it-dot-com",
        "teknaf-to-tetulia",
        "digital-generation",
        "campus",
        "lifestyle"
    ]

    # all_url.append([complete_url])

    for d in All_date:
        for cat in cat_list:
            complete_url = base_address + '/' + str(d) + '/' + cat + '/'
            print(complete_url)
            all_url.append([complete_url])
            pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()


    ##########################################2222222222222222222222######################################
    ########################################## 2nd part ##################################################

    import bs4
    import requests
    import csv

    global all_unit_link
    all_unit_link = []
    main_page_links = []

    # base_address = "https://www.jugantor.com"
    # category = "national"

    def get_sub_links(main_page_link, path, listbox_selected_category):

        print(main_page_link)
        global all_unit_link, all_category
        # print(main_page_link)
        page = requests.get(main_page_link)
        # print(page)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)

        newsArticleDivs = soup.find_all("div", {"class": "col-12 col-md-9"})  # "row margin-bottom-40"}) # "col-md-8"}) # "col-md-7-5 col-sm-7-5" }) # "col-md-8 col-sm-8"}) #"col-md-8"}) # "col-md-7-5 col-sm-7-5"})
        # print(newsArticleDivs)
        # col-md-7-5 col-sm-7-5 # last used
        # col - md - 3
        # col-md-8 col-sm-8 output no. 190
        # col-md-6 col-sm-6 additional-nav

        for newsArticle in newsArticleDivs:

            li = newsArticle.find_all("div", {"class": "list-article"})
            # print(li)
            i = 0
            for l in li:
                a_tag = l.find("a")
                news_link = a_tag['href']
                if news_link == "javascript:;":
                    continue
                print(news_link)

                for cate in listbox_selected_category:
                    cate = str(cate)
                    for date in All_date:
                        if date in main_page_link:
                            if cate in main_page_link:
                                print(cate)
                                print(date)
                                all_category.append(cate)
                                complete_url = "https://www.dailyjanakantha.com/" + news_link
                                all_unit_link.append([complete_url, cate, date])


                # print(news_link)
                # complete_url = base_address + news_link[1:]
                '''
                complete_url = "https://www.dailyjanakantha.com/" + news_link
                all_unit_link.append([complete_url])
                '''

        # print("Hello world.")

        pass
        # print(all_unit_link)

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='w', newline='', encoding='utf-8') as unit_url_list:
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

    for main_link in main_page_links:
        # print(main_link)
        try:
            get_sub_links(main_link, path, listbox_selected_category)
        except:
            pass
        pass

    write_csv(all_unit_link, path, listbox_selected_category)

    print(len(all_unit_link))

    ############################################333333333333333333333###############################
    ############################################ 3rd part ##########################################

    import bs4
    import requests
    import csv
    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    CSV_LINK = 'January_December_2018_all_make_csv_sports.csv'

    def append_to_csv(row, path, category):
        global CSV_LINK
        if category == 'All':
            CSV_LINK = path + "/Janakantha_" + category + "_news.csv"
        else:
            CSV_LINK = path + "/Janakantha_" + category + "_news.csv"

        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, news_category, news_date, path, listbox_selected_category):
        BASE_URL = url
        page = requests.get(BASE_URL)
        date = BASE_URL[41:51]
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)

        newsTitle = soup.find_all("h1")[0].getText()
        print(newsTitle)
        article_text = soup.find("div", {"class": "article-details mb-5"})
        all_paragraphs = article_text("p")
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()
        # print(news_content)
        #input_array = [newsTitle, news_content, date, news_category]
        for cat in listbox_selected_category:
            cat = str(cat)
            if cat==news_category:
                input_array = [news_date, newsTitle, news_content, cat]
                append_to_csv(input_array, path, cat)

        input_array = [news_date, newsTitle, news_content, news_category]
        append_to_csv(input_array, path, 'All')

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            # if i >= 5:
            #   break
            print(i)
            try:
                get_title_and_content(row[0], row[1], row[2], path, listbox_selected_category)
            except:
                pass
            i += 1
