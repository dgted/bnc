

def function1(start_date, end_date, path, listbox_selected_category):
    import bs4
    import requests
    import csv
    import pandas as pd
    from datetime import datetime

    print(start_date)
    print(end_date)
    start_date = str(start_date)
    month, date, year = start_date.split("/")
    if len(month)==1:
        month = "0"+month
    if len(date)==1:
        date = "0"+date
    #print(month)
    #print(date)
    year = "20"+year
    #print(year)
    start_date = year+"/"+month+"/"+date

    end_date = str(end_date)
    month1, date1, year1 = end_date.split("/")
    if len(month1)==1:
        month1 = "0"+month1
    if len(date1)==1:
        date1 = "0"+date1
    print(month1)
    print(date1)
    year1 = "20"+year1
    print(year1)
    end_date = year1+"/"+month1+"/"+date1

    print(start_date)
    print(end_date)

    print("Jugantor")
    print(listbox_selected_category)

    a = pd.date_range(start=start_date, end=end_date).to_pydatetime().tolist()
    All_date = []
    for i in a:
        d = str(i)
        d = d.replace("-", '/')
        All_date.append(d[0:10])

    base_address = "https://www.jugantor.com/archive/print-edition"

    all_url = []

    complete_url = base_address
    print(complete_url)

    # all_url.append([complete_url])

    for d in All_date:
        complete_url = base_address + '/' + str(d)
        print(complete_url)
        all_url.append([complete_url])
        pass

    with open(path+'/all_Archive_main_page_url.csv', mode='w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()

    ###2222222222222222222222222222222222222222222222222
    ####222222-2018 archive
    import bs4
    import requests
    import csv

    all_unit_link = []
    date_list = []
    main_page_links = []
    C = 0

    def get_sub_links(date, main_page_link, path, listbox_selected_category):
        global all_unit_link
        # print(main_page_link)
        page = requests.get(main_page_link)
        # print(page)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        # newsArticleDivs = soup.find_all("div", {"class": "row"},limit=20

        newsArticleDivs = soup.find_all("div", {"class": "pre-scrollable archive-newslist"})

        for ul in newsArticleDivs:
            UL = ul.find_all('li')
            # print(UL)
            for p in UL:
                a_tag = p.find('a')
                #print("///////////////////////")
                # print(a_tag)
                news_link = a_tag['href']

                print(news_link)
                # complete_url = base_address + news_link[1:]


                if (len(listbox_selected_category) >= 1):
                    if len(listbox_selected_category)==1:
                        if listbox_selected_category[0] in news_link:
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==2:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==3:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==4:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==5:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==6:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==7:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==8:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==9:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==10:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link) or (listbox_selected_category[9] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==11:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link) or (listbox_selected_category[9] in news_link) or (listbox_selected_category[10] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==12:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link) or (listbox_selected_category[9] in news_link) or (listbox_selected_category[10] in news_link) or (listbox_selected_category[11] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==13:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link) or (listbox_selected_category[9] in news_link) or (listbox_selected_category[10] in news_link) or (listbox_selected_category[11] in news_link) or (listbox_selected_category[12] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==14:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link) or (listbox_selected_category[9] in news_link) or (listbox_selected_category[10] in news_link) or (listbox_selected_category[11] in news_link) or (listbox_selected_category[12] in news_link) or (listbox_selected_category[13] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==15:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link) or (listbox_selected_category[9] in news_link) or (listbox_selected_category[10] in news_link) or (listbox_selected_category[11] in news_link) or (listbox_selected_category[12] in news_link) or (listbox_selected_category[13] in news_link) or (listbox_selected_category[14] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)

                    elif len(listbox_selected_category)==16:
                        if (listbox_selected_category[0] in news_link) or (listbox_selected_category[1] in news_link) or (listbox_selected_category[2] in news_link) or (listbox_selected_category[3] in news_link) or (listbox_selected_category[4] in news_link) or (listbox_selected_category[5] in news_link) or (listbox_selected_category[6] in news_link) or (listbox_selected_category[7] in news_link) or (listbox_selected_category[8] in news_link) or (listbox_selected_category[9] in news_link) or (listbox_selected_category[10] in news_link) or (listbox_selected_category[11] in news_link) or (listbox_selected_category[12] in news_link) or (listbox_selected_category[13] in news_link) or (listbox_selected_category[14] in news_link) or (listbox_selected_category[15] in news_link):
                            complete_url = news_link[0:]
                            write_csv(date, complete_url, path, listbox_selected_category)


                ####if All is selected as category #####################
                if ((len(listbox_selected_category)==1) and (listbox_selected_category[0]=="All")):
                    complete_url = news_link[0:]
                    """ Pure URL Are Collecting"""
                    S = str(complete_url)
                    # print(len("https://www.bd-journal.com/bangladesh/1"))
                    write_csv(date, complete_url, path, listbox_selected_category)


        pass

    def write_csv(date, list_to_be_inserted, path, listbox_selected_category):
        with open(path+'/all_Archive_unit_page_url.csv', mode='a', newline='', encoding='utf-8') as unit_url_list:
            unit_url_writer = csv.writer(unit_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            unit_url_writer.writerow([date, list_to_be_inserted])

        unit_url_list.close()
        pass

    with open(path+'/all_Archive_main_page_url.csv') as main_url_csv:
        readCSV = csv.reader(main_url_csv)

        for row in readCSV:
            link = row[0]
            date = (link[50:])
            print(link)
            print(date)

            get_sub_links(date, link, path, listbox_selected_category)
            pass

    print('+---------------------------------------------------------+')

    # write_csv(all_unit_link,date_list)

    print(len(all_unit_link))

    ####3333333333333333333333333333all-national_content
    ############ 3rd part ############################################################
    ##################################################################################

    import bs4
    import requests
    import csv

    URL_LINK = path + '/all_Archive_unit_page_url.csv'
    CSV_LINK = '/Content_Jugantor_'

    def append_to_csv(row, path, latest_category):
        global CSV_LINK
        with open(path+"/"+"Jugantor_"+ latest_category +"_news.csv", mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
        # news_article_writer.close()
        pass

    def get_title_and_content(url, date, path, listbox_selected_category):
        BASE_URL = url
        page = requests.get(BASE_URL)

        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        #print(soup)
        try:
            newsTitle = soup.find_all("h5")[0].getText()
        except:
            pass

        article_text = soup.find("div", {"class": "text-justify my-2 pr-md-4"})
        all_paragraphs = article_text("p")
        news_content = ""
        for paragraph in all_paragraphs:
            news_content += paragraph.getText()

        #print(news_content)

        '''
        if current_category=="first-page news":
            if 'first-page' in url:
                input_array = [date, newsTitle, news_content, 'first-page_news']
                print(news_content)
                append_to_csv(input_array, path, 'first-page_news')

        if current_category=="last-page news":
            if 'last-page' in url:
                input_array = [date, newsTitle, news_content, 'last-page news']
                print(news_content)
                append_to_csv(input_array, path, 'last-page news')

        if current_category=="sports":
            if 'sports' in url:
                input_array = [date, newsTitle, news_content, 'sports']
                print(news_content)
                append_to_csv(input_array, path, 'sports')

        if current_category=="editorial":
            if 'editorial' in url:
                input_array = [date, newsTitle, news_content, 'editorial']
                print(news_content)
                append_to_csv(input_array, path, 'editorial')

        if current_category=="national":
            if 'news' in url:
                input_array = [date, newsTitle, news_content, 'national']
                print(news_content)
                append_to_csv(input_array, path, 'national')

        if current_category=="international":
            if 'ten-horizon' in url:
                input_array = [date, newsTitle, news_content, 'international']
                print(news_content)
                append_to_csv(input_array, path, 'international')

        if current_category=="entertainment":
            if 'anando-nagar' in url:
                input_array = [date, newsTitle, news_content, 'entertainment']
                print(news_content)
                append_to_csv(input_array, path, 'entertainment')

        if current_category=="second-edition news":
            if 'second-edition' in url:
                input_array = [date, newsTitle, news_content, 'second-edition news']
                print(news_content)
                append_to_csv(input_array, path, 'second-edition news')

        if current_category=="sub-editorial":
            if 'sub-editorial' in url:
                input_array = [date, newsTitle, news_content, 'sub-editorial']
                print(news_content)
                append_to_csv(input_array, path, 'sub-editorial')

        if current_category=="bangla-face":
            if 'bangla-face' in url:
                input_array = [date, newsTitle, news_content, 'bangla-face']
                print(news_content)
                append_to_csv(input_array, path, 'bangla-face')

        if current_category=="City news":
            if 'city' in url:
                input_array = [date, newsTitle, news_content, 'City']
                print(news_content)
                append_to_csv(input_array, path, 'City')

        if current_category=="Bad news":
            if 'obituary' in url:
                input_array = [date, newsTitle, news_content, 'Bad']
                print(news_content)
                append_to_csv(input_array, path, 'Bad')

        if current_category=="literature-magazine":
            if 'literature-magazine' in url:
                input_array = [date, newsTitle, news_content, 'literature-magazine']
                print(news_content)
                append_to_csv(input_array, path, 'literature-magazine')

        if current_category=="death-aniverary":
            if 'deate-aniverary' in url:
                input_array = [date, newsTitle, news_content, 'death-aniverary']
                print(news_content)
                append_to_csv(input_array, path, 'death-aniverary')

        if current_category=="letter":
            if 'letter' in url:
                input_array = [date, newsTitle, news_content, 'letter']
                print(news_content)
                append_to_csv(input_array, path, 'letter')

        if current_category=="islam-and-life":
            if 'islam-and-life' in url:
                input_array = [date, newsTitle, news_content, 'islam-and-life']
                print(news_content)
                append_to_csv(input_array, path, 'islam-and-life')
                
        '''



        if ((len(listbox_selected_category)==1) and (listbox_selected_category[0]=="All")):
            global temp_category
            if 'first-page' in url:
                temp_category = 'first-page'

            elif 'last-page' in url:
                temp_category = 'last-page'

            elif 'sports' in url:
                temp_category = 'sports'

            elif 'editorial' in url:
                temp_category = 'editorial'

            elif 'news' in url:
                temp_category = 'news'

            elif 'ten-horizon' in url:
                temp_category = 'ten-horizon'

            elif 'anando-nagar' in url:
                temp_category = 'anando-nagar'

            elif 'second-edition' in url:
                temp_category = 'second-edition'

            elif 'sub-editorial' in url:
                temp_category = 'sub-editorial'

            elif 'bangla-face' in url:
                temp_category = 'bangla-face'

            elif 'city' in url:
                temp_category = 'city'

            elif 'obituary' in url:
                temp_category = 'obituary'

            elif 'literature-magazine' in url:
                temp_category = 'literature-magazine'

            elif 'deate-aniverary' in url:
                temp_category = 'death-aniverary'

            elif 'letter' in url:
                temp_category = 'letter'

            elif 'islam-and-life' in url:
                temp_category = 'islam-and-life'

            input_array = [date, newsTitle, news_content, temp_category]
            #print(news_content)
            append_to_csv(input_array, path, 'All')


            if 'first-page' in url:
                input_array = [date, newsTitle, news_content, 'first-page']
                #print(news_content)
                append_to_csv(input_array, path, 'first-page')

            elif 'last-page' in url:
                input_array = [date, newsTitle, news_content, 'last-page']
                #print(news_content)
                append_to_csv(input_array, path, 'last-page')

            elif 'sports' in url:
                input_array = [date, newsTitle, news_content, 'sports']
                #print(news_content)
                append_to_csv(input_array, path, 'sports')

            elif 'editorial' in url:
                input_array = [date, newsTitle, news_content, 'editorial']
                #print(news_content)
                append_to_csv(input_array, path, 'editorial')

            elif 'news' in url:
                input_array = [date, newsTitle, news_content, 'news']
                #print(news_content)
                append_to_csv(input_array, path, 'news')

            elif 'ten-horizon' in url:
                input_array = [date, newsTitle, news_content, 'ten-horizon']
                #print(news_content)
                append_to_csv(input_array, path, 'ten-horizon')

            elif 'anando-nagar' in url:
                input_array = [date, newsTitle, news_content, 'anando-nagar']
                #print(news_content)
                append_to_csv(input_array, path, 'anando-nagar')

            elif 'second-edition' in url:
                input_array = [date, newsTitle, news_content, 'second-edition']
                #print(news_content)
                append_to_csv(input_array, path, 'second-edition')

            elif 'sub-editorial' in url:
                input_array = [date, newsTitle, news_content, 'sub-editorial']
                #print(news_content)
                append_to_csv(input_array, path, 'sub-editorial')

            elif 'bangla-face' in url:
                input_array = [date, newsTitle, news_content, 'bangla-face']
                #print(news_content)
                append_to_csv(input_array, path, 'bangla-face')

            elif 'city' in url:
                input_array = [date, newsTitle, news_content, 'city']
                #print(news_content)
                append_to_csv(input_array, path, 'city')

            elif 'obituary' in url:
                input_array = [date, newsTitle, news_content, 'obituary']
                #print(news_content)
                append_to_csv(input_array, path, 'obituary')

            elif 'literature-magazine' in url:
                input_array = [date, newsTitle, news_content, 'literature-magazine']
                #print(news_content)
                append_to_csv(input_array, path, 'literature-magazine')

            elif 'deate-aniverary' in url:
                input_array = [date, newsTitle, news_content, 'death-aniverary']
                #print(news_content)
                append_to_csv(input_array, path, 'death-aniverary')

            elif 'letter' in url:
                input_array = [date, newsTitle, news_content, 'letter']
                #print(news_content)
                append_to_csv(input_array, path, 'letter')

            elif 'islam-and-life' in url:
                input_array = [date, newsTitle, news_content, 'islam-and-life']
                #print(news_content)
                append_to_csv(input_array, path, 'islam-and-life')




        #3rd part total news collection if multiple category is selected
        if (len(listbox_selected_category) >= 1) and not((len(listbox_selected_category)==1) and (listbox_selected_category[0]=="All")):
            global all_temp_category
            if 'first-page' in url:
                all_temp_category = 'first-page'

            elif 'last-page' in url:
                all_temp_category = 'last-page'

            elif 'sports' in url:
                all_temp_category = 'sports'

            elif 'editorial' in url:
                all_temp_category = 'editorial'

            elif 'news' in url:
                all_temp_category = 'news'

            elif 'ten-horizon' in url:
                all_temp_category = 'ten-horizon'

            elif 'anando-nagar' in url:
                all_temp_category = 'anando-nagar'

            elif 'second-edition' in url:
                all_temp_category = 'second-edition'

            elif 'sub-editorial' in url:
                all_temp_category = 'sub-editorial'

            elif 'bangla-face' in url:
                all_temp_category = 'bangla-face'

            elif 'city' in url:
                all_temp_category = 'city'

            elif 'obituary' in url:
                all_temp_category = 'obituary'

            elif 'literature-magazine' in url:
                all_temp_category = 'literature-magazine'

            elif 'deate-aniverary' in url:
                all_temp_category = 'deate-aniverary'

            elif 'letter' in url:
                all_temp_category = 'letter'

            elif 'islam-and-life' in url:
                all_temp_category = 'islam-and-life'

            input_array = [date, newsTitle, news_content, all_temp_category]
            #print(news_content)
            append_to_csv(input_array, path, 'All_Selected_Categories')
            ###





            if 'first-page' in url:
                input_array = [date, newsTitle, news_content, 'first-page']
                #print(news_content)
                append_to_csv(input_array, path, 'first-page')

            elif 'last-page' in url:
                input_array = [date, newsTitle, news_content, 'last-page']
                #print(news_content)
                append_to_csv(input_array, path, 'last-page')

            elif 'sports' in url:
                input_array = [date, newsTitle, news_content, 'sports']
                #print(news_content)
                append_to_csv(input_array, path, 'sports')

            elif 'editorial' in url:
                input_array = [date, newsTitle, news_content, 'editorial']
                #print(news_content)
                append_to_csv(input_array, path, 'editorial')

            elif 'news' in url:
                input_array = [date, newsTitle, news_content, 'news']
                #print(news_content)
                append_to_csv(input_array, path, 'news')

            elif 'ten-horizon' in url:
                input_array = [date, newsTitle, news_content, 'ten-horizon']
                #print(news_content)
                append_to_csv(input_array, path, 'ten-horizon')

            elif 'anando-nagar' in url:
                input_array = [date, newsTitle, news_content, 'anando-nagar']
                #print(news_content)
                append_to_csv(input_array, path, 'anando-nagar')

            elif 'second-edition' in url:
                input_array = [date, newsTitle, news_content, 'second-edition']
                #print(news_content)
                append_to_csv(input_array, path, 'second-edition')

            elif 'sub-editorial' in url:
                input_array = [date, newsTitle, news_content, 'sub-editorial']
                #print(news_content)
                append_to_csv(input_array, path, 'sub-editorial')

            elif 'bangla-face' in url:
                input_array = [date, newsTitle, news_content, 'bangla-face']
                #print(news_content)
                append_to_csv(input_array, path, 'bangla-face')

            elif 'city' in url:
                input_array = [date, newsTitle, news_content, 'city']
                #print(news_content)
                append_to_csv(input_array, path, 'city')

            elif 'obituary' in url:
                input_array = [date, newsTitle, news_content, 'obituary']
                #print(news_content)
                append_to_csv(input_array, path, 'obituary')

            elif 'literature-magazine' in url:
                input_array = [date, newsTitle, news_content, 'literature-magazine']
                #print(news_content)
                append_to_csv(input_array, path, 'literature-magazine')

            elif 'deate-aniverary' in url:
                input_array = [date, newsTitle, news_content, 'death-aniverary']
                #print(news_content)
                append_to_csv(input_array, path, 'death-aniverary')

            elif 'letter' in url:
                input_array = [date, newsTitle, news_content, 'letter']
                #print(news_content)
                append_to_csv(input_array, path, 'letter')

            elif 'islam-and-life' in url:
                input_array = [date, newsTitle, news_content, 'islam-and-life']
                #print(news_content)
                append_to_csv(input_array, path, 'islam-and-life')

            ##

        pass

    with open(URL_LINK, encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i = 0
        for row in readCSV:
            i += 1
            date = row[0]
            link = row[1]
            #print(link)

            if i >= 0:
                try:
                    get_title_and_content(link, date, path, listbox_selected_category)
                except:
                    pass
                print(i)


