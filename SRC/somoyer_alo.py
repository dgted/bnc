

def Somoyer_Alo(start_date, end_date, path, listbox_selected_category):
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

    # https://www.kalerkantho.com/print-edition/first-page/2020/12/01
    #https://www.shomoyeralo.com/archive.php?date=2020-04-06
    base_address = "https://www.shomoyeralo.com/archive.php?date="

    all_url = []

    complete_url = base_address
    print(complete_url)

    # all_url.append([complete_url])


    for d in All_date:
        complete_url = base_address + str(d)
        print(complete_url)
        all_url.append([complete_url])
        pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    ################################### 222222222222222222222222 #####################################
    ################################### 2nd part #####################################################

    import bs4
    import requests
    import csv
    global all_unit_link, main_page_links
    all_unit_link = []
    main_page_links = []
    base_address = "https://www.shomoyeralo.com"  # same
    category = "cat.php?cd=120&pg="  # same

    def get_sub_links(main_page_link, path, listbox_selected_category):
        global all_unit_link
        page = requests.get(main_page_link)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        #print(soup)
        newsArticleDivs = soup.find_all("div", {"class": "bullet"})
        for newsArticle in newsArticleDivs:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = base_address + '/' + news_link
            for date in All_date:
                date = str(date)
                if date in main_page_link:
                    print(complete_url)
                    all_unit_link.append([complete_url, date])
        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='w',newline='') as unit_url_list:  # each page each news category
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
        get_sub_links(main_link, path, listbox_selected_category)
        pass
    write_csv(all_unit_link, path, listbox_selected_category)
    print(len(all_unit_link))

    ################################# 333333333333333333333333333 #####################################
    ################################# 3rd part ########################################################

    import bs4
    import requests
    import csv

    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    CSV_LINK = 'ShomoerAlo.csv'  # follow

    def append_to_csv(row, path, category):

        global CSV_LINK
        CSV_LINK = path + "/Somoyer-Alo_" + category + "_news.csv"

        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            news_article_writer.writerow(row)

        # news_article_writer.close()

        pass

    def get_title_and_content(url, news_date, path, listbox_selected_category):
        BASE_URL = url
        page = requests.get(BASE_URL)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')

        print(soup)

        newsTitle = soup.find_all("title")[0].getText()
        # print(newsTitle)
        article_text = soup.find("div", {"id": "f"})

        news_content = article_text.getText()

        # print(news_content)

        input_array = [news_date, newsTitle, news_content, 'All']  # change it for categery naming

        append_to_csv(input_array, path, 'All')

        pass

    with open(URL_LINK) as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)

        i = 0

        for row in readCSV:
            try:
                get_title_and_content(row[0], row[1], path, listbox_selected_category)
                print(i)
                i += 1
            except:
                print('exception occured')


