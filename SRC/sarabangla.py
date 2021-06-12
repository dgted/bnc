

def SARABANGLA(s, e, path, listbox_selected_category):
    s = int(s)
    e = int(e)

    if s<e:
        small = s
        large = e
    else:
        small = e
        large = s



    print(s)
    print(e)
    print(path)
    print(listbox_selected_category)

    import bs4
    import requests
    import csv

    base_address = "https://sarabangla.net"
    category = "archive"

    all_url = []

    complete_url = base_address + "/" + category + "/"
    print(complete_url)
    all_url.append([complete_url])

    # page/9602/
    page = large + 1

    for i in range(small, page):
        complete_url = base_address + '/' + category + '/page/' + str(i) + "/"
        # print(complete_url)
        all_url.append([complete_url])
    pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    ###########################2nd##########################

    # importing necessary libraries

    global main_page_links, all_unit_link

    main_page_links = []
    all_unit_link = []
    dateOfNews = []

    base_address = "https://sarabangla.net"

    # category = "parliament/24"

    # to get all sub links from a main link
    def get_sub_links(main_page_link, path, listbox_selected_category):
        global all_unit_link
        page = requests.get(main_page_link)

        # why
        p = int(page.status_code)
        while p != 200:
            print(page.status_code)
            page = requests.get(main_page_link)
            p = int(page.status_code)
        # print(page)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        newsArticleDivs = soup.find_all("div", {"class": "col-md-9 col-sm-9 col-xs-7 padding-left-10"})
        # news_DateUls = soup.find_all("ul", {"class": "list-inline newsinfo hidden-xs"})

        newsDate = 0

        for newsArticle in newsArticleDivs:
            demo_list = []

            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            demo_list.append(complete_url)

            ''''
            i_Date = news_DateUls[newsDate].find_all("li")
            newsDate += 1
            try:
                # print(li_Date[1].text)
                demo_list.append(str(li_Date[1].text))
            except:
                demo_list.append(str(1))
             '''
            all_unit_link.append(demo_list)

        pass

    def write_csv(list_to_be_inserted, path, listbox_selected_category):
        # print(list_to_be_inserted)
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

    # get_sub_links(main_page_links[2])

    i = 1
    for main_link in main_page_links:
        if i <= 0:
            i += 1
            continue
        try:
            get_sub_links(main_link, path, listbox_selected_category)
        except:
            pass
        i = i + 1
        pass

    print(str(i - 1) + " done !")

    write_csv(all_unit_link, path, listbox_selected_category)

    print(len(all_unit_link))

    ###################3rd#################################

    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    CSV_LINK = 'all_news.csv'

    def append_to_csv(row, path, category):
        global CSV_LINK
        CSV_LINK = path + "/Sara-Bangla_" + category + "_news.csv"
        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, path, listbox_selected_category):

        # print("#################################")
        # print(url)

        BASE_URL = url
        page = requests.get(BASE_URL)

        # if server failed
        p = int(page.status_code)
        while p != 200:
            print(page.status_code)
            page = requests.get(BASE_URL)
            p = int(page.status_code)
        # print(type(page.status_code))

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        newsTitle = soup.find_all("title")[0].getText()
        print(newsTitle)
        article_text = soup.find("div", {"class": "single_content"})
        # print(article_text)
        all_paragraphs = article_text("p")
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        if news_content in "":
            news_content = article_text.getText()

        print("-------------------------------------------")
        print(news_content)

        input_array = [newsTitle, news_content, 'All']
        append_to_csv(input_array, path, 'All')
        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            if i < 0:
                i += 1
                continue
            print(i)
            # print(row[0],row[1])
            try:
                get_title_and_content(row[0], path, listbox_selected_category)
            except:
                pass

            i += 1


