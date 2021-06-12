

def naya_diganta(start_date, end_date, path, listbox_selected_category):
    import bs4
    import requests
    import csv
    import pandas as pd
    from datetime import datetime

    print(start_date)
    print(end_date)
    print(path)
    print(listbox_selected_category)

    global All_date
    a = pd.date_range(start=start_date, end=end_date).to_pydatetime().tolist()
    All_date = []
    for i in a:
        d = str(i)
        All_date.append(d[0:10])

    base_address = "https://www.dailynayadiganta.com/archive"

    all_url = []

    complete_url = base_address
    print(complete_url)

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




    #####################22222222222222222222222######################
    # importing necessary libraries
    import bs4
    import requests
    import csv

    main_page_links = []
    all_unit_link = []

    base_address = "https://www.dailynayadiganta.com"



    # to get all sub links from a main link
    def get_sub_links(main_page_link, path, listbox_selected_category):
        global all_unit_link, new_list, cat_list, temp_list, All_date, Date_list
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(All_date)
        temp_list = []
        cat_list = []
        all_unit_link = []
        new_list = []
        Date_list = []
        page = requests.get(main_page_link)

        # why
        p = int(page.status_code)
        while p != 200:
            print(page.status_code)
            page = requests.get(main_page_link)
            p = int(page.status_code)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        #print(soup)
        newsArticleDivs = soup.find_all("ol", {"class": "margin archive-news-list"})

        if "All" in listbox_selected_category:
            temp_list = ["election", "Incident-accident", "politics", "crime", "parliament", "economics", "education", "diplomacy", "law-and-justice", "climate", "disaster", "Festival", "administration", "subcontinent", "asia", "middle-east", "turkey", "usa-canada", "uk", "europe", "africa", "america", "australia", "international-organizations", "cricket", "football", "athletics", "tennis", "dhaka", "chattagram", "rajshahi", "khulna", "rangpur", "mymensingh", "sylhet", "barishal", "sub-editorial", "opinion", "health", "cinema", "television", "music", "art-literature", "science-tech", "social%20media%20corner", "History%20and%20Tradition", "religion", "Expatriate", "nature-environment", "plant-animal"]

        else:
            #temp_list = []
            if "todays-paper" in listbox_selected_category:
                cat_list = ["first-page", "last-page", "editorial", "post-editorial", "city", "onnodiganta", "diganta-islami-jobon", "daily", "bangla-diganta", "more-news", "satrong"]
                temp_list.extend(cat_list)
                cat_list = []

            if "national" in listbox_selected_category:
                cat_list = ["election", "Incident-accident", "politics", "crime", "parliament", "economics", "education", "diplomacy", "law-and-justice", "climate", "disaster", "Festival", "administration"]
                temp_list.extend(cat_list)
                cat_list = []

            if "international" in listbox_selected_category:
                cat_list = ["subcontinent", "asia", "middle-east", "turkey", "usa-canada", "uk", "europe", "africa", "america", "australia", "international-organizations"]
                temp_list.extend(cat_list)
                cat_list = []

            if "sports" in listbox_selected_category:
                cat_list = ["cricket", "football", "athletics", "tennis"]
                temp_list.extend(cat_list)
                cat_list = []

            if "country" in listbox_selected_category:
                cat_list = ["dhaka", "chattagram", "rajshahi", "khulna", "rangpur", "mymensingh", "sylhet", "barishal"]
                temp_list.extend(cat_list)
                cat_list = []

            if "sub-editorial" in listbox_selected_category:
                cat_list = ["sub-editorial", "opinion"]
                temp_list.extend(cat_list)
                cat_list = []

            if "lifestyle" in listbox_selected_category:
                cat_list = ["health"]
                temp_list.extend(cat_list)
                cat_list = []

            if "entertainment" in listbox_selected_category:
                cat_list = ["cinema", "television", "music"]
                temp_list.extend(cat_list)
                cat_list = []

            if "others" in listbox_selected_category:
                cat_list = ["art-literature", "science-tech", "social%20media%20corner", "History%20and%20Tradition", "religion", "Expatriate", "nature-environment", "plant-animal"]
                temp_list.extend(cat_list)
                cat_list = []



        for newsArticle in newsArticleDivs:
            LI = newsArticle.find_all('li')
            for li in LI:
                a_tag = li.find('a')
                news_link = a_tag['href']
                print(news_link)
                complete_url = news_link[0:]

                for date in All_date:
                    date = str(date)
                    if date in main_page_link:
                        y = date
                        Date_list.append(y)
                        print(y)

                for i in temp_list:
                    i = str(i)
                    if i in complete_url:
                        new_list.append([complete_url])


                #new_list.append([complete_url])
            write_csv(new_list, path, listbox_selected_category)

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

    i = 1
    for main_link in main_page_links:
        if i <= 0:
            i += 1
            continue
        get_sub_links(main_link, path, listbox_selected_category)
        i = i + 1
        pass

    print(str(i - 1) + " done !")



    ####################################################3rd part ############################################

    import bs4
    import requests
    import csv

    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    #CSV_LINK = 'diganta-islami-jobon_all_news.csv'

    def append_to_csv(row, path, category):
        global CSV_LINK
        CSV_LINK = path + "/Nayadiganta_"+category+"_news.csv"
        with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        pass


    def get_title_and_content(url, path, listbox_selected_category):
        global Date_list, di
        #print("INNNNNNNNNNNNNNNNNSIDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        #print(Date_list)
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
        #print(newsTitle)
        article_text = soup.find("div", {"class": "news-content"})
        # print(article_text)
        all_paragraphs = article_text("p")
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        if news_content in "":
            news_content = article_text.getText()

        #print("-------------------------------------------")
        #print(news_content)

        news_Date = "2020-02-02"

        #news_Date = Date_list[di]
        #print(di)
        #di += 1

        if (("first-page" in url) or ("last-page" in url) or ("editorial" in url) or ("post-editorial" in url) or ("city" in url) or ("onnodiganta" in url) or ("diganta-islami-jobon" in url) or ("daily" in url) or ("bangla-diganta" in url) or ("more-news" in url) or ("satrong" in url)):
            category = "todays-paper"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        if (("election" in url) or ("Incident-accident" in url) or ("politics" in url) or ("crime" in url) or ("parliament" in url) or ("economics" in url) or ("education" in url) or ("diplomacy" in url) or ("law-and-justice" in url) or ("climate" in url) or ("disaster" in url) or ("Festival" in url) or ("administration" in url)):
            category = "national"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        if (("cricket" in url) or ("football" in url) or ("athletics" in url) or ("tennis" in url) or ("sports" in url)):
            category = "sports"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        if (("dhaka" in url) or ("chattagram" in url) or ("rajshahi" in url) or ("khulna" in url) or ("rangpur" in url) or ("mymensingh" in url) or ("sylhet" in url) or ("barishal" in url)):
            category = "country"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)


        if (("sub-editorial" in url) or ("opinion" in url)):
            category = "sub-editorial"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        if (("health" in url)):
            category = "lifestyle"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        if (("cinema" in url) or ("television" in url) or ("music" in url)):
            category = "entertainment"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        if (("art-literature" in url) or ("science-tech" in url) or ("social%20media%20corner" in url) or ("History%20and%20Tradition" in url) or ("religion" in url) or ("Expatriate" in url) or ("nature-environment" in url) or ("plant-animal" in url)):
            category = "others"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        if (("subcontinent" in url) or ("asia" in url) or ("middle-east" in url) or ("turkey" in url) or ("usa-canada" in url) or ("uk" in url) or ("europe" in url) or ("africa" in url) or ("america" in url) or ("australia" in url) or ("international-organizations" in url)):
            category = "international"
            input_array = [news_Date, newsTitle, news_content, category]
            append_to_csv(input_array, path, category)

        #category = 'Todays-paper'

        input_array = [news_Date, newsTitle, news_content, category]
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
                print("Not Found")
                pass

            i += 1



