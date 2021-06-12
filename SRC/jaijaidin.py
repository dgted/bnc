
def Jaijaidin(s, e, Path, listbox_selected_category):
    print("/////]]]]]")
    print(s)

    global path
    current_category = listbox_selected_category
    path = Path
    for i in listbox_selected_category:
        print(i)

    # 1111111111111---2018 archive
    import bs4
    import requests
    import csv
    import pandas as pd
    from datetime import datetime

    a = pd.date_range(start=s, end=e).to_pydatetime().tolist()

    base_address = "https://www.jaijaidinbd.com/archive"

    all_url = []

    complete_url = base_address
    print(complete_url)

    global All_date
    # all_url.append([complete_url])
    a = pd.date_range(start=s, end=e).to_pydatetime().tolist()
    All_date = []
    for i in a:
        d = str(i)
        d = d.replace("-", '/')
        All_date.append(d[0:10])

    for d in All_date:
        complete_url = base_address + '/' + str(d[0:10])
        print(complete_url)
        all_url.append([complete_url])
        pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            # print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    ####222222-2020 archive reserve

    all_unit_link = []
    date_list = []
    main_page_links = []
    C = 0

    def append_to_csv(row, Date, current_category, path):
        CSV_LINK = '/all_Archive_unit_page_url.csv'
        with open(path + "/" + CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow([Date, row, current_category])
        # news_article_writer.close()
        pass

    def get_sub_links(main_page_link, date, current_category, path):

        global all_unit_link
        # print(main_page_link)
        try:
            page = requests.get(main_page_link)
        except:
            pass
        # print(page)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        # newsArticleDivs = soup.find_all("div", {"class": "row"},limit=20

        newsArticleDivs = soup.find_all("div", {"class": "col-md-6 col-sm-6"})
        # print(newsArticleDivs)

        l = 0
        for newsArticle in newsArticleDivs:
            UL = newsArticle.find_all('ul')
            for Li in UL:

                a_tag = Li.find('a')
                news_link = a_tag['href']

                print(news_link)
                for cat in current_category:
                    string = str(cat)
                    if cat in news_link:
                        for Date in All_date:
                            Date = str(date)
                            if date in main_page_link:
                                print(Date)
                                append_to_csv(news_link, Date, string, path)

        """"

         """

    with open(path + '/all_Archive_main_page_url.csv') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            c = 'https://www.bd-journal.com/archive/online-edition/2020/01/01'
            date = row[0]
            date = date[50:]

            main_page_links.append(row[0])
            date_list.append(date)

    print('+---------------------------------------------------------+')

    for main_link in main_page_links:
        try:
            get_sub_links(main_link, date_list[C], current_category, path)
        except:
            pass
        print(C)

        C = C + 1

    """3rd part """
    ####3333333333333333333333333333all-national_content
    import bs4
    import requests
    import csv
    URL_LINK = path + '/all_Archive_unit_page_url.csv'

    def append_to_csv(row, category, path):
        global CSV_LINK
        with open(path + "/" + category + ".csv", mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, date, Now_categ, path):
        BASE_URL = url
        page = requests.get(BASE_URL)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        newsTitle = soup.find_all("h1")[0].getText()
        article_text = soup.find("div", {"class": "dtl_hl_block"})
        all_paragraphs = article_text("p")
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        for i in listbox_selected_category:

            string = str(i)

            if string in url:
                entry = [date, newsTitle, news_content, string]
                append_to_csv(entry, "Jay_jay_Din_" + string, path)
                append_to_csv(entry, "Jay_jay_Din_all", path)

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            i += 1
            date = row[0]
            link = row[1]
            CATEG = row[2]

            if i >= 0:
                try:
                    get_title_and_content(link, date, CATEG, path)
                except:
                    pass
                print(i)

    """ 3rd part end"""
