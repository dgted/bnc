
def BD24LIVE(s, e, Path, listbox_selected_category):
    s = int(s)
    e = int(e)

    if s<e:
        small = s
        large = e
    else:
        small = e
        large = s

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





    base_address = "https://www.bd24live.com/bangla/archive/page/"

    all_url = []

    complete_url = base_address


    for i in range(small , large +1 ,1):


        if(i==1):
            all_url.append(["https://www.bd24live.com/bangla/archive"])
            print("https://www.bd24live.com/bangla/archive")
        else:
            complete_url = base_address +str(i ) +"/"
            all_url.append([complete_url])
            print(complete_url)



    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    ####222222-2020 archive reserve

    all_unit_link = []
    date_list = []
    main_page_links = []
    C = 0

    def append_to_csv(row, current_category, path):
        CSV_LINK = '/all_Archive_unit_page_url.csv'
        with open(path + "/" + CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow([ row, current_category])
        # news_article_writer.close()
        pass

    def get_sub_links(main_page_link, current_category, path):

        global all_unit_link
        # print(main_page_link)
        page = requests.get(main_page_link)
        # print(page)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        # newsArticleDivs = soup.find_all("div", {"class": "row"},limit=20

        newsArticleDivs_Left = soup.find_all("div", {"class": "width50 left category-news"})
        newsArticleDivs_Right = soup.find_all("div", {"class": "width50 right category-news"})

        # print(newsArticleDivs)

        l = 0
        for newsArticle in newsArticleDivs_Right:
            l = l + 1
            print(l)

            print("==========================")
            Left =newsArticle.find('a')

            news_link = Left['href']
            print(news_link)
            append_to_csv(news_link ,"All", path)

            print("==========================")

        for newsArticle in newsArticleDivs_Left:

            l = l + 1
            print(l)
            print("==========================")
            Left =newsArticle.find('a')

            news_link = Left['href']
            print(news_link)
            append_to_csv(news_link ,"All", path)

            print("==========================")



            # print(news_link)

            # append_to_csv(news_link, date,"All", path)

        """"

         """

    with open(path + '/all_Archive_main_page_url.csv') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            c = 'https://www.bd-journal.com/archive/online-edition/2020/01/01'

            main_page_links.append(row[0])

    print('+---------------------------------------------------------+')

    for main_link in main_page_links:
        try:
            get_sub_links(main_link, current_category, path)
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

    def get_title_and_content(url, Now_categ, path):
        BASE_URL = url
        page = requests.get(BASE_URL)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        try:
            newsTitle = soup.find_all("h1")[0].getText()
            article_text = soup.find("div", {"class": "width100 details-news"})
            all_paragraphs = article_text("p")
        except :
            pass


        news_content = ""
        try:
            for paragraph in all_paragraphs:
                news_content += paragraph.getText()
        except:
            pass


        entry = [ newsTitle, news_content ,"All_news"]

        append_to_csv(entry, "BD24LIVE_All_news", path)

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            i += 1
            try:
                link = row[0]
                cate = row[1]
            except:
                pass


            if i >= 0:
                try:
                    get_title_and_content(link ,cate, path)
                except:
                    pass
                print(i)

    """ 3rd part end"""