

def daily_sangram(start_date, end_date, path, listbox_selected_category):
    import bs4
    import requests
    import csv
    import pandas as pd
    from datetime import datetime

    print(start_date)
    print(end_date)
    print(path)
    print(listbox_selected_category)
    global Sangram_all
    global first_url
    Sangram_all = [
        "first-page",
        "editorial",
        "international",
        "village-town",
        "sports",
        "economy-trade",
        "last-page",
        "body-health",
        "womens-world",
        "literature",
        "blue-greens-hut",
        "religion-life",
        "city%20revolution",
        "society-culture",
        "variegated",
        "world-revolution",
        "free-stage",
        "great-silhet",
        "games-sports",
        "agriculture-industry"
    ]

    a = pd.date_range(start=start_date, end=end_date).to_pydatetime().tolist()
    All_date = []
    for i in a:
        d = str(i)
        #d = d.replace("-", '/')
        All_date.append(d[0:10])

    base_address = "https://dailysangram.com/page/"

    all_url = []

    for i in Sangram_all:
        i = str(i)
        first_url = base_address + i

        for d in All_date:
            complete_url = first_url + '/' + str(d)

            for parse_cat in listbox_selected_category:
                if parse_cat in complete_url:
                    print(complete_url)
                    all_url.append([complete_url])
                    pass


    with open(path+'/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()


    #complete_url = base_address
    #print(complete_url)

    ###2222222222222222222222222222222222222222222222222
    ####222222-2018 archive
    import bs4
    import requests
    import csv
    global all_unit_link, main_page_links, cat, cat_list
    all_unit_link = []
    main_page_links = []
    cat_list = []
    abc = []


    def get_sub_links(main_page_link, path, listbox_selected_category):
        print("mainpagelink****")
        print(main_page_link)
        global all_unit_link, cat, cat_list

        try:
            page = requests.get(main_page_link)
        except:
            pass

        try:
            soup = bs4.BeautifulSoup(page.content, 'html.parser')
        except:
            pass
        # print(soup)
        try:
            newsArticleDivs = soup.find_all("li", {"class": "even"})
        except:
            pass

        try:
            newsArticleLiOdd = soup.find_all("li", {"class": "odd"})
        except:
            pass

        p = 0
        for newsArticle in newsArticleDivs:
            # print(newsArticle)
            print(p)
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            # complete_url = base_address + news_link[1:]
            complete_url = news_link[0:]
            print(complete_url)

            for i in listbox_selected_category:
                if i in main_page_link:
                    cat = i
            print(cat)
            cat_list.append(cat)

            all_unit_link.append([complete_url])
            p = p + 1

        for newsArticle in newsArticleLiOdd:
            # print(newsArticle)
            print(p)
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            # complete_url = base_address + news_link[1:]
            complete_url = news_link[0:]
            print(complete_url)

            for i in listbox_selected_category:
                if i in main_page_link:
                    cat = i
            print(cat)
            cat_list.append(cat)

            all_unit_link.append([complete_url])
            p = p + 1
        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='w', newline='', encoding='utf-8') as unit_url_list:
            unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for url in list_to_be_inserted:
                # print(url)
                unit_url_writer.writerow(url)

        unit_url_list.close()

        pass

    with open(path+'/all_Archive_main_page_url.csv', encoding='utf-8') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            main_page_links.append(row[0])

    print('+---------------------------------------------------------+')

    # get_sub_links(main_page_links[5])

    for main_link in main_page_links:
        get_sub_links(main_link, path, listbox_selected_category)
        pass

    write_csv(all_unit_link, path, listbox_selected_category)



    ################################# 3rd #######################################
    import bs4
    import requests
    import csv

    #global iteration
    #iteration = 0

    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    CSV_LINK = 'thesis_dataset_dailySangram_new.csv'

    def append_to_csv(row, path, category):

        global CSV_LINK
        if category=='All':
            CSV_LINK = path+"/Sangram_"+category+"_Selected_Categories_news.csv"
        else:
            CSV_LINK = path + "/Sangram_" + category + "_news.csv"



        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            news_article_writer.writerow(row)

        # news_article_writer.close()

        pass

    def get_title_and_content(url, path, listbox_selected_category, index):
        BASE_URL = url
        page = requests.get(BASE_URL)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')

        try:
            newsTitle = soup.find_all("h1")[0].getText()
        except:
            pass
        #print(newsTitle)
        article_text = soup.find("div", {"class": "postBody"})

        article_text_time = soup.find("div", {"class": "postInfo"}).getText()
        # article_text_time = soup.find("p", {"class": "dateTime"}).getText()
        #print(article_text_time)

        all_paragraphs = article_text("p")

        news_content = ""
        news_date = ""

        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        #print("news: @@@@@   " + news_content)
        news_type = cat_list[index]

        for selected_cat in listbox_selected_category:
            if selected_cat==cat_list[index]:
                news_type = cat_list[index]
                input_array = [article_text_time, newsTitle, news_content, news_type]
                append_to_csv(input_array, path, str(news_type))



        input_array = [article_text_time, newsTitle, news_content, news_type]

        append_to_csv(input_array, path, 'All')

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 1
        for row in readCSV:
            # if i > 2:
            # break

            print(i)
            try:
                get_title_and_content(row[0], path, listbox_selected_category, i-1)
            except:
                pass
            i += 1

