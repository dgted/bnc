

def Odhikar_News(start_date, end_date, path, listbox_selected_category):
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
        d = d.replace("-", '/')
        All_date.append(d[0:10])

    #https://www.odhikar.news/archive/2020/12/01
    # https://www.kalerkantho.com/print-edition/first-page/2020/12/01
    base_address = "https://www.odhikar.news/archive"

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


    ############################### 22222222222222222222222222222 ######################################
    ############################### 2nd part ###########################################################

    global all_unit_link, main_page_links
    # creating two lists
    # main_page_links to extract from csv and store all main links
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
        print(soup)
        newsArticleDivs = soup.find_all("div", {"class": "col-md-6 col-sm-6"})

        for newsArticle in newsArticleDivs:
            a_tag = newsArticle.find("a")
            try:
                news_link = a_tag['href']
                complete_url = news_link[0:]
                print(complete_url)
                for selected_cat in listbox_selected_category:
                    selected_cat = str(selected_cat)
                    if selected_cat in complete_url:
                        for date in All_date:
                            date = str(date)
                            if date in main_page_link:
                                all_unit_link.append([complete_url, date])

            except:
                print("link not available")

        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='w', newline='', encoding='utf-8') as unit_url_list:
            unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for url in list_to_be_inserted:
                print(url)
                unit_url_writer.writerow(url)
        unit_url_list.close()
        pass

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

    ################################# 33333333333333333333333333 ################################
    ################################# 3rd part ##################################################

    def append_to_csv(row, path, category):
        global NEWS_CSV_LINK
        if category == 'All':
            NEWS_CSV_LINK = path + "/Doinik_Odhikar_" + category + "_news.csv"
        else:
            NEWS_CSV_LINK = path + "/Doinik_Odhikar_" + category + "_news.csv"
        with open(NEWS_CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, news_date, path, listbox_selected_category):
        BASE_URL = url

        page = requests.get(BASE_URL)
        p = int(page.status_code)

        while p != 200:
            print(page.status_code)
            page = requests.get(BASE_URL)
            p = int(page.status_code)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        newsTitle = soup.find_all("title")[0].getText()
        newsTitle = newsTitle.strip()
        # ----------------------------------------------Date--------------------------------------------------
        newswriter = soup.find("div", {"class": "rpt_and_share_block"})
        newswriter = newswriter("p")[0].getText()
        newswriter = newswriter.strip()
        print(newswriter)
        date = soup.find("div", {"class": "rpt_and_share_block"})
        date = date.getText()
        date = date.replace(newswriter, "")
        date = date.strip()
        print(date)

        # ----------------------------------------------------------------------------------------------------
        print(newsTitle)
        article_text = soup.find("div", {"id": "myText"})
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

        print("-----")
        print(news_content[0:70])

        for cat in listbox_selected_category:
            cat = str(cat)
            if cat in url:
                cat_all = cat
                input_array = [news_date, newsTitle, news_content, cat]
                append_to_csv(input_array, path, cat)


        input_array = [news_date, newsTitle, news_content, cat_all]
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
                get_title_and_content(row[0], row[1], path, listbox_selected_category)
            except:
                pass
            i += 1
            pass
        print("All done")



