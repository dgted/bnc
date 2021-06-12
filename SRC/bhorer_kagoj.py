

def Bhorer_Kagoj(start_date, end_date, path, listbox_selected_category):
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

    base_address = "https://www.bhorerkagoj.com"

    all_url = []

    complete_url = base_address
    print(complete_url)

    for d in All_date:
        complete_url = base_address + '/' + str(d)+ '/'
        print(complete_url)
        all_url.append([complete_url])
        pass

    with open(path + '/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    #################################### 2222222222222222222222222222 ############################
    #################################### 2nd part ################################################

    import bs4
    import requests
    import csv

    global all_unit_link, main_page_links

    all_unit_link = []
    main_page_links = []

    def get_sub_links(main_page_link, path, listbox_selected_category):

        global all_unit_link

        page = requests.get(main_page_link)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')

        newsArticleDivs = soup.find_all("div", {"class": "col-sm-6 col-xs-12"})

        for newsArticle in newsArticleDivs:
            a_tag = newsArticle.find("a")
            news_link = a_tag['href']
            complete_url = news_link[0:]
            print(complete_url)
            all_unit_link.append([complete_url])

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

    ########################## 333333333333333333333333333333333333 ##########################
    ############################### 3rd part #################################################

    import bs4
    import requests
    import csv
    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    CSV_LINK = 'thesis_dataset_sarabangla_new.csv'

    def append_to_csv(row, path, category):
        global CSV_LINK
        CSV_LINK = path + "/Bhorer-Kagoj_" + category + "_news.csv"
        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, path, listbox_selected_category):
        BASE_URL = url
        page = requests.get(BASE_URL)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        try:

            newsTitle = soup.find_all("h2")[0].getText()
            print(newsTitle)
            date = soup.find("div", {"class": "col-md-4", "style": "border-left: 2px solid #ccc; border-right: 2px solid #ccc;"}).getText()
            print(date)
            article_text = soup.find("div", {"id": "content-p"})
            all_paragraphs = article_text("p")
        except:
            print("Error")
        # print(all_paragraphs)
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()
        print(news_content)

        for news_date in All_date:
            news_date = str(news_date)
            if news_date in url:
                input_array = [newsTitle, news_content, date, 'All']
                append_to_csv(input_array, path, 'All')

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            if (i > -1):
                try:
                    print(i)
                    get_title_and_content(row[0], path, listbox_selected_category)
                except:
                    pass
            i += 1



