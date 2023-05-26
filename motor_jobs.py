from bs4 import BeautifulSoup
import requests
import re

class Jobs:

    def clear_tag(self, txt):
        return str(txt).replace("\n", "").replace("\t", "").replace("\b", "")

    def profession(self, txt):
        return str(txt).replace(" ","+")

    def get_job(self):
        return [self.details_job(job["href"])\
            for job in self.pages.findAll(class_="thumbnail") \
                if job.get('href') and 'empregacampinas.' in job.get('href')]
            

    def details_job(self, url):
        web = BeautifulSoup(requests.get(url).text, "lxml")
        html = web.find(class_="col-lg-8 conteudo-vaga")

        details = []
        details.append(self.clear_tag(html.h1.span.text).strip())

        for count, topic in enumerate(html.findAll("p")):
            if count == 2 or count == 3 or count == 4 or count == 5 \
               or count == 6:
                    details.append(topic.text)
            elif(count >= 7):
                try:
                    self.valid_email_and_phone(details, topic.text)
                except Exception as erro:
                    print("SEM CONTATO", erro)
        return (details[0], details[3][8:], details[4][11:], details[1][19:],
                     details[2][12:], details[6], url)

    def valid_email_and_phone(self, details, txt):
        check = ["^([1-9]{2}) 9[7-9]{1}[0-9]{3}-[0-9]{4}$",
                  "[a-zA-Z0-9]+[a-zA-Z0-9_.-]+@{1}[a-zA-Z0-9_.-]*\\.+[a-z]{2,4}"]
        for page in range(2):
            try:
                details.append(re.findall(check[page], txt)[0])
            except Exception as erro:
                ...
                
    def browser(self, profession, page):
        url = "http://empregacampinas.com.br/page/{}/?s={}".format(page, self.profession(profession))
        self.pages = BeautifulSoup(requests.get(url).text, "lxml")
        return self.get_job()

    def __str__(self):
        return self.pages.text
    
# buscador = Jobs()    
# print(buscador.browser('professor', 1))