

def United_News_Bd(start_date, end_date, path, listbox_selected_category):
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

    base_address = "https://unb.com.bd/bangla/allnews?date="

    all_url = []

    complete_url = base_address
    print(complete_url)

    # all_url.append([complete_url])

    all_num = ["","&page=1","&page=2","&page=3","&page=4","&page=5"]

    for d in All_date:
        for num in all_num:
            complete_url = base_address + str(d) + num
            print(complete_url)
            all_url.append([complete_url])
            pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    ###################################### 22222222222222222222222 ########################################
    ###################################### 2nd part #######################################################

    import bs4
    import requests
    import csv

    global all_unit_link, main_page_links

    all_unit_link = []
    main_page_links = []

    base_address = "http://unb.com.bd/bangla"
    category = "category/6/বিশ্ব"

    def get_sub_links(main_page_link, path, listbox_selected_category):

        global all_unit_link
        # print(main_page_link)
        page = requests.get(main_page_link)
        # print(page)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        # newsArticleDivs = soup.find_all("div", {"class": "col-xs-12 col-sm-6 col-md-6 n_row"})
        newsArticleDivs = soup.find_all("h3", {"class": "h3-edit"})

        for newsArticle in newsArticleDivs:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            # print(news_link)
            # complete_url = base_address + news_link[1:]
            complete_url = news_link[0:]
            print(complete_url)
            for selected_cat in listbox_selected_category:
                selected_cat = str(selected_cat)
                if selected_cat in complete_url:
                    for date in All_date:
                        date = str(date)
                        if date in main_page_link:
                            all_unit_link.append([complete_url, date])
            # print(all_unit_link)

        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='w', newline='', encoding='utf-8') as unit_url_list:
            unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for url in list_to_be_inserted:
                print(url)
                unit_url_writer.writerow(url)

        unit_url_list.close()

        pass

    with open(path+'/all_Archive_main_page_url.csv') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            main_page_links.append(row[0])

    print('+---------------------------------------------------------+')

    for main_link in main_page_links:
        try:
            get_sub_links(main_link, path, listbox_selected_category)
        except:
            pass
        pass

    write_csv(all_unit_link, path, listbox_selected_category)

    print(len(all_unit_link))


    ################################# 3333333333333333333333333333 ###################################
    ################################### 3rd part #####################################################

    import bs4
    import requests
    import csv
    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    CSV_LINK = 'world_dataset_new.csv'

    def append_to_csv(row, path, category):
        global CSV_LINK
        if category == 'সব-খবর':
            CSV_LINK = path + "/United-News-bd_" + category + "_news.csv"
        else:
            CSV_LINK = path + "/United-News-bd_" + category + "_news.csv"

        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, news_date, path, listbox_selected_category):
        BASE_URL = url
        page = requests.get(BASE_URL)
        date = BASE_URL[41:51]
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        #print(soup)

        newsTitle = soup.find_all("h1")[0].getText()
        
        article_text = soup.find_all("div", {"class": "news-article-text-block text-patter-edit"})

        for w in article_text:
            if 'p' not in w:
                first = w.getText()
            t = w.find_all('p')
            news_content = ""
            if 'p' not in w:
                news_content = news_content + first

            if 'p' in w:
                for paragraph in t:
                    news_content += paragraph.getText()

        #print(news_content)
        #print("------------------------------------------------------------------")

        for cat in listbox_selected_category:
            cat = str(cat)
            if cat in url:
                cat_all = cat
                input_array = [news_date, newsTitle, news_content, cat]
                append_to_csv(input_array, path, cat)

        input_array = [news_date, newsTitle, news_content, cat_all]
        append_to_csv(input_array, path, 'সব-খবর')

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            try:
                print(i)
                get_title_and_content(row[0], row[1], path, listbox_selected_category)
            except:
                pass
            i += 1

