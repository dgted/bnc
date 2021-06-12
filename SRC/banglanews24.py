


def bangla_news24(start_date, end_date, path, listbox_selected_category):
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
        # d = d.replace("-", '/')
        All_date.append(d[0:10])
    # https://www.banglanews24.com/archive_news_list/2020-12-17
    # https: // www.banglanews24.com / archive_news_list / 2020 - 12 - 17?page = 2

    base_address = "https://www.banglanews24.com/archive_news_list"
    all_url = []

    complete_url = base_address
    print(complete_url)

    # all_url.append([complete_url])

    for d in All_date:
        complete_url = base_address + '/' + str(d)
        print(complete_url)
        all_url.append([complete_url])
        pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    ##################################### 2222222222222222222222222 ###################################
    ##################################### 2nd part ####################################################

    import bs4
    import requests
    import csv

    global all_unit_link, main_page_links

    all_unit_link = []
    main_page_links = []
    # https://www.banglanews24.com/archive_news_list/2020-12-17
    # https: // www.banglanews24.com / archive_news_list / 2020 - 12 - 17?page = 2
    base_address = "https://www.banglanews24.com"
    category = "film?page="

    def get_sub_links(main_page_link, path, listbox_selected_category):
        global all_unit_link

        page = requests.get(main_page_link)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        newsArticleDivs = soup.find_all("div", {"class": "col-md-4"})

        for newsArticle in newsArticleDivs:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            # print(news_link)
            complete_url = news_link[0:]
            print(complete_url)

            # for date in All_date:
            #     date = str(date)
            #     if date in main_page_link:
            #         all_unit_link.append([complete_url, date])
            for selected_cat in listbox_selected_category:
                selected_cat = str(selected_cat)
                for date in All_date:
                    date = str(date)
                    if date in main_page_link:
                        if selected_cat in complete_url:
                            all_unit_link.append([complete_url, date])

        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path + '/all_Archive_unit_page_url.csv', mode='w', newline='', encoding='utf-8') as unit_url_list:
            unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for url in list_to_be_inserted:
                print(url)
                unit_url_writer.writerow(url)

        unit_url_list.close()

        pass

    with open(path + '/all_Archive_main_page_url.csv', encoding='utf-8') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            main_page_links.append(row[0])

    print('+---------------------------------------------------------+')

    # get_sub_links(main_page_links[5])

    for main_link in main_page_links:
        try:
            get_sub_links(main_link, path, listbox_selected_category)
        except:
            pass
        pass

    write_csv(all_unit_link, path, listbox_selected_category)

    print(len(all_unit_link))

    ##################################### 3333333333333333333333 ###############################
    ##################################### 3rd part #############################################

    import bs4
    import requests
    import csv
    # https://www.banglanews24.com/archive_news_list/2020-12-17
    # https: // www.banglanews24.com / archive_news_list / 2020 - 12 - 17?page = 2

    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    # URL_LINK = "all_Archive_unit_page_url.csv"
    CSV_LINK = 'film_news.csv'

    def append_to_csv(row, path, category):

        global CSV_LINK
        if category == 'All':
            CSV_LINK = path + "/BanglaNews24_" + category + "_news.csv"
        else:
            CSV_LINK = path + "/BanglaNews24_" + category + "_news.csv"

        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            news_article_writer.writerow(row)

        # news_article_writer.close()

        pass

    def get_title_and_content(url, news_date, path, listbox_selected_category):
        print("333333333333333333333333333333")
        BASE_URL = url
        page = requests.get(BASE_URL)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')

        newsTitle = soup.find_all("h1")[1].getText()
        article_text = soup.find("article")
        ads = soup.find_all('div', class_='ads')
        for x in ads:
            x.extract()
        all_paragraphs = article_text("p")
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        # newsTitle = soup.find_all("h1")[1].getText()
        # article_text = soup.find("article")
        # all_paragraphs = article_text("p")
        # news_content = ""
        #
        # for paragraph in all_paragraphs:
        #     news_content += paragraph.getText()
        print(newsTitle)
        print(news_content)
        for cat in listbox_selected_category:
            cat = str(cat)
            if cat in url:
                cat_all = cat
                input_array = [news_date, newsTitle, news_content, cat]
                append_to_csv(input_array, path, cat)

        input_array = [news_date, newsTitle, news_content, cat_all]

        append_to_csv(input_array, path, 'All')

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            try:
                get_title_and_content(row[0], row[1], path, listbox_selected_category)
                print(i)
                print(row[0], row[1])
                i += 1
            except:
                print('exception occured')
