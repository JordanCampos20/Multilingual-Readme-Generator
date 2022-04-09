from googletrans import Translator
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import re

translator = Translator()

githubusername = ''
githubnickname = ''
icon = ''
title = ''
subtitle = ''
linktodownloadproject = ''
linktoviewproject = ''
explanation_running = ''
technologies = ''
libraries = ''
photoprofile = ''

#Change
while True:

    try:
        choice = input(Fore.LIGHTRED_EX + ' Select Language (1 = English, 2 = Portuguese, 3 = Japonese, 4 = Korean, 5 = Chinese, 6 = Chinese Traditional, 0 = Close): ')

        if choice == '0':
            quit()

        if choice == '1':
            try:
                print('-------------------------')
                print('English')
                githubusername = input(Fore.LIGHTRED_EX + 'Your Username the URL (Default: JordanCampos20): ')
                res = re.findall(r'\w+', githubusername)
                if githubusername == '':
                    githubusername = 'JordanCampos20'

                elif githubusername.startswith('https://github.com'):
                    githubusername = res[3]
                    o = Options()
                    o.add_argument('--headless')
                    s = Service('C:\\Users\\OWO\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                else:
                    o = Options()
                    o.add_argument('--headless')
                    s = Service('C:\\Users\\OWO\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()

                githubnickname = input(Fore.LIGHTRED_EX + 'Your Nickname (Default: Jordan C.): ')
                if githubnickname == '':
                    githubnickname = 'Jordan C.'
                print('-------------------------')
                icon = input(Fore.LIGHTRED_EX + 'Icon (Default: 🌐️): ')
                if icon == '':
                    icon = '🌐️'
                title = input(Fore.LIGHTRED_EX + 'Title: ')
                if title == '':
                    title = 'Title'
                subtitle = input(Fore.LIGHTRED_EX + 'Subtitle: ')
                if subtitle == '':
                    subtitle = 'Subtitle'
                linktodownloadproject = input(Fore.LIGHTRED_EX + 'Project name on Github: ')
                if linktodownloadproject == '':
                    linktodownloadproject = 'PROJECT-NAME-IN-GITHUB'
                linktoviewproject = input(Fore.LIGHTRED_EX + 'Site Link Have: ')
                if linktoviewproject == '':
                    linktoviewproject = 'SITE-LINK'
                explanation_running = input(Fore.LIGHTRED_EX + 'Explanation of How to Run the Project: ')
                if explanation_running == '':
                    explanation_running = 'XPLICATION OF HOW TO RUN THE CODE'
                technologies = input(Fore.LIGHTRED_EX + 'Used Technologies, Like Programs or Languages: ')
                if technologies == '':
                    technologies = 'PROGRAMS OR LANGUAGES YOU USED TO MAKE THE CODE'
                libraries = input(Fore.LIGHTRED_EX + 'Used Libraries: ')
                if libraries == '':
                    libraries = "LIBRARIES YOU'VE USED"
                print(Fore.CYAN + 'Creating the Readme.md...')
                break
            except:
                print('something went wrong')

        if choice == '2':
            try:
                print('-------------------------')
                print('Portuguese')
                githubusername = input(Fore.LIGHTRED_EX + 'Seu nome de usuário na URL (Padrão: JordanCampos20): ')
                res = re.findall(r'\w+', githubusername)
                if githubusername == '':
                    githubusername = 'JordanCampos20'

                elif githubusername.startswith('https://github.com'):
                    githubusername = res[3]
                    o = Options()
                    o.add_argument('--headless')
                    s = Service('C:\\Users\\OWO\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                else:
                    o = Options()
                    o.add_argument('--headless')
                    s = Service('C:\\Users\\OWO\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()

                githubnickname = input(Fore.LIGHTRED_EX + 'Seu Apelido (Padrão: Jordan C.): ')
                if githubnickname == '':
                    githubnickname = 'Jordan C.'
                print('-------------------------')
                icon = input(Fore.LIGHTRED_EX + 'Icone (Padrão: 🌐️): ')
                if icon == '':
                    icon = '🌐️'
                title = input(Fore.LIGHTRED_EX + 'Titulo: ')
                if title == '':
                    title = 'TITULO'
                subtitle = input(Fore.LIGHTRED_EX + 'Subtitulo: ')
                if subtitle == '':
                    subtitle = 'SUBTITULO'
                linktodownloadproject = input(Fore.LIGHTRED_EX + 'Nome do Projeto no Github: ')
                if linktodownloadproject == '':
                    linktodownloadproject = 'NOME-DO-PROJETO-NO-GITHUB'
                linktoviewproject = input(Fore.LIGHTRED_EX + 'Link do Site Tiver: ')
                if linktoviewproject == '':
                    linktoviewproject = 'LINK-DO-SITE'
                explanation_running = input(Fore.LIGHTRED_EX + 'Explicação de Como Executar o Projeto: ')
                if explanation_running == '':
                    explanation_running = 'EXPLICACAO DE COMO EXECUTAR O CODIGO'
                technologies = input(Fore.LIGHTRED_EX + 'Tecnologias Usadas, Como Programas ou Linguagens: ')
                if technologies == '':
                    technologies = 'PROGRAMAS OU LINGUAGENS QUE VOCE USOU PARA FAZER O CODIGO'
                libraries = input(Fore.LIGHTRED_EX + 'Bibliotecas Usadas: ')
                if libraries == '':
                    libraries = 'BIBLIOTECAS QUE VOCE USOU'
                print(Fore.CYAN + 'Criando os Readme.md...')
                break
            except:
                print('algo deu errado')

        if choice == '3':
            try:
                print('-------------------------')
                print('Japonese')
                githubusername = input(Fore.LIGHTRED_EX + 'ユーザー名URL（デフォルト: JordanCampos20）: ')
                res = re.findall(r'w+', githubusername)
                if githubusername == '':
                    githubusername = 'JordanCampos20'

                elif githubusername.startswith('https://github.com'):
                    githubusername = res[3]
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                else:
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                githubnickname = input(Fore.LIGHTRED_EX + 'あなたのニックネーム（デフォルト: Jordan C.）:  ')
                if githubnickname == '':
                    githubnickname = 'Jordan C.'
                print('-------------------------')
                icon = input(Fore.LIGHTRED_EX + 'アイコン（デフォルト: 🌐️）: ')
                if icon == '':
                    icon = '🌐️'
                title = input(Fore.LIGHTRED_EX + 'タイトル: ')
                if title == '':
                    title = 'タイトル'
                subtitle = input(Fore.LIGHTRED_EX + 'キャプション: ')
                if subtitle == '':
                    subtitle = 'キャプション'
                linktodownloadproject = input(Fore.LIGHTRED_EX + 'Githubのプロジェクト名: ')
                if linktodownloadproject == '':
                    linktodownloadproject = 'PROJECT-NAME-ON-GITHUB'
                linktoviewproject = input(Fore.LIGHTRED_EX + 'ウェブサイトのリンクがあります: ')
                if linktoviewproject == '':
                    linktoviewproject = 'ウェブサイトへのリンク'
                explanation_running = input(Fore.LIGHTRED_EX + 'プロジェクトの実行方法の説明:')
                if explanation_running == '':
                    explanation_running = 'コードを実行する方法の説明'
                technologies = input(Fore.LIGHTRED_EX + 'プログラムや言語など、使用されるテクノロジー: ')
                if technologies == '':
                    technologies = 'コードを作成するために使用したプログラムまたは言語'
                libraries = input(Fore.LIGHTRED_EX + '使用するライブラリ: ')
                if libraries == '':
                    libraries = '使用したライブラリ'
                print(Fore.CYAN + 'Readme.mdを作成しています...')
                break
            except:
                print('何かがうまくいかなかった')

        if choice == '4':
            try:
                print('-------------------------')
                print('Korean')
                githubusername = input(Fore.LIGHTRED_EX + '사용자 이름 URL(기본값: JordanCampos20): ')
                res = re.findall(r'w+', githubusername)
                if githubusername == '':
                    githubusername = 'JordanCampos20'

                elif githubusername.startswith('https://github.com'):
                    githubusername = res[3]
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                else:
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                githubnickname = input(Fore.LIGHTRED_EX + '닉네임(기본값: Jordan C.): ')
                if githubnickname == '':
                    githubnickname = 'Jordan C.'
                print('-------------------------')
                icon = input(Fore.LIGHTRED_EX + '아이콘(기본값: 🌐️): ')
                if icon == '':
                    icon = '🌐️'
                title = input(Fore.LIGHTRED_EX + '제목: ')
                if title == '':
                    title = '제목'
                subtitle = input(Fore.LIGHTRED_EX + '표제: ')
                if subtitle == '':
                    subtitle = '표제'
                linktodownloadproject = input(Fore.LIGHTRED_EX + 'Github의 프로젝트 이름: ')
                if linktodownloadproject == '':
                    linktodownloadproject = '프로젝트 이름-ON-GITHUB'
                linktoviewproject = input(Fore.LIGHTRED_EX + '웹사이트 링크: ')
                if linktoviewproject == '':
                    linktoviewproject = '웹 사이트 링크'
                explanation_running = input(Fore.LIGHTRED_EX + '프로젝트 실행 방법에 대한 설명: ')
                if explanation_running == '':
                    explanation_running = '코드 실행 방법에 대한 설명'
                technologies = input(Fore.LIGHTRED_EX + '프로그램 또는 언어와 같은 사용 기술: ')
                if technologies == '':
                    technologies = '코드를 만드는 데 사용한 프로그램 또는 언어'
                libraries = input(Fore.LIGHTRED_EX + '사용된 라이브러리: ')
                if libraries == '':
                    libraries = '당신이 사용한 라이브러리'
                print(Fore.CYAN + 'Readme.md 생성 중...')
                break
            except:
                print('문제가 발생했습니다.')

        if choice == '5':
            try:
                print('-------------------------')
                print('Chinese')
                githubusername = input(Fore.LIGHTRED_EX + '您的用户名 URL（默认: JordanCampos20）: ')
                res = re.findall(r'w+', githubusername)
                if githubusername == '':
                    githubusername = 'JordanCampos20'

                elif githubusername.startswith('https://github.com'):
                    githubusername = res[3]
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                else:
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                githubnickname = input(Fore.LIGHTRED_EX + '您的昵称（默认: Jordan C.）: ')
                if githubnickname == '':
                    githubnickname = 'Jordan C.'
                print('-------------------------')
                icon = input(Fore.LIGHTRED_EX + '图标（默认: 🌐️）: ')
                if icon == '':
                    icon = '🌐️'
                title = input(Fore.LIGHTRED_EX + '标题: ')
                if title == '':
                    title = '标题'
                subtitle = input(Fore.LIGHTRED_EX + '标题: ')
                if subtitle == '':
                    subtitle = '标题'
                linktodownloadproject = input(Fore.LIGHTRED_EX + 'Github 上的项目名称: ')
                if linktodownloadproject == '':
                    linktodownloadproject = '项目名称在 GITHUB'
                linktoviewproject = input(Fore.LIGHTRED_EX + '网站链接有: ')
                if linktoviewproject == '':
                    linktoviewproject = '网站链接'
                explanation_running = input(Fore.LIGHTRED_EX + '如何运行项目的说明: ')
                if explanation_running == '':
                    explanation_running = '如何运行代码的说明'
                technologies = input(Fore.LIGHTRED_EX + '使用的技术，例如程序或语言: ')
                if technologies == '':
                    technologies = '您用于编写代码的程序或语言'
                libraries = input(Fore.LIGHTRED_EX + '使用的库: ')
                if libraries == '':
                    libraries = '您使用过的库'
                print(Fore.CYAN + '正在创建 Readme.md...')
                break
            except:
                print('有些不对劲')

        if choice == '6':
            try:
                print('-------------------------')
                print('Chinese Traditional')
                githubusername = input(Fore.LIGHTRED_EX + '您的用戶名 URL（默認: JordanCampos20）: ')
                res = re.findall(r'w+', githubusername)
                if githubusername == '':
                    githubusername = 'JordanCampos20'

                elif githubusername.startswith('https://github.com'):
                    githubusername = res[3]
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                else:
                    o = Options()
                    o.add_argument('--headless')
                    s = Service(r'C:\Users\OWO\AppData\Local\Programs\Python\chromedriver.exe')
                    browser = webdriver.Chrome(service=s, options=o)
                    browser.get(f"https://github.com/{githubusername}/")
                    sleep(2)
                    images = browser.find_element(by=By.CSS_SELECTOR, value="div.js-profile-editable-replace img")
                    photoprofile = images.get_attribute("src")
                    browser.close()
                githubnickname = input(Fore.LIGHTRED_EX + '您的暱稱（默認: Jordan C.）: ')
                if githubnickname == '':
                    githubnickname = 'Jordan C.'
                print('-------------------------')
                icon = input(Fore.LIGHTRED_EX + '圖標（默認: 🌐️）: ')
                if icon == '':
                    icon = '🌐️'
                title = input(Fore.LIGHTRED_EX + '標題: ')
                if title == '':
                    title = '標題'
                subtitle = input(Fore.LIGHTRED_EX + '標題: ')
                if subtitle == '':
                    subtitle = '標題'
                linktodownloadproject = input(Fore.LIGHTRED_EX + 'Github 上的項目名稱: ')
                if linktodownloadproject == '':
                    linktodownloadproject = '項目名稱在 GITHUB'
                linktoviewproject = input(Fore.LIGHTRED_EX + '網站鏈接有: ')
                if linktoviewproject == '':
                    linktoviewproject = '網站鏈接'
                explanation_running = input(Fore.LIGHTRED_EX + '如何運行項目的說明: ')
                if explanation_running == '':
                    explanation_running = '如何運行代碼的說明'
                technologies = input(Fore.LIGHTRED_EX + '使用的技術，例如程序或語言: ')
                if technologies == '':
                    technologies = '您用於編寫代碼的程序或語言'
                libraries = input(Fore.LIGHTRED_EX + '使用的庫: ')
                if libraries == '':
                    libraries = '您使用過的庫'
                print(Fore.CYAN + '正在創建 Readme.md...')
                break
            except:
                print('出問題了')

        else:
            print('Language Unavailable, Idioma Indisponível, 言語は利用できません, 사용할 수 없는 언어, 语言不可用, 語言不可用')
            continue

    except (KeyboardInterrupt):
        quit()

#No Change
altimage = 'Preview do Projeto'
text_link_to_view_project = 'Clique para ver o projeto'
text_link_to_download_project = 'Clique para baixar o projeto'
installation = 'Instalação'
python_explanation = 'Se você tiver python2 e python3, use pip3 ao fazer o download de requirements.txt'
running = 'Executando'
technologies_used = 'Tecnologias utilizadas'
explanation_technologies_used = 'Para o desenvolvimento deste aplicativo utilizei as seguintes technologies:'
used_library = 'Bibliotecas Usadas'
explanation_used_library = 'Para o desenvolvimento deste aplicativo utilizei as seguintes libraries:'
author = 'Autor'

#English Translation
titulotraducaoen = translator.translate(title, dest='en')
subtitulotraducaoen = translator.translate(subtitle, dest='en')
altdaimagemtraducaoen = translator.translate(altimage, dest='en')
text_link_to_download_projecttraducaoen = translator.translate(text_link_to_download_project, dest='en')
text_link_to_view_projecttraducaoen = translator.translate(text_link_to_view_project, dest='en')
installationtraducaoen = translator.translate(installation, dest='en')
python_explanationtraducaoen = translator.translate(python_explanation, dest='en')
runningtraducaoen = translator.translate(running, dest='en')
explicao_runningtraducaoen = translator.translate(explanation_running, dest='en')
technologies_usedtraducaoen = translator.translate(technologies_used, dest='en')
explanation_technologies_usedtraducaoen = translator.translate(explanation_technologies_used, dest='en')
used_librarytraducaoen = translator.translate(used_library, dest='en')
explanation_used_librarytraducaoen = translator.translate(explanation_used_library, dest='en')
authortraducaoen = translator.translate(author, dest='en')

#Portuguese Translation
titulotraducaopt = translator.translate(title, dest='pt')
subtitulotraducaopt = translator.translate(subtitle, dest='pt')
altdaimagemtraducaopt = translator.translate(altimage, dest='pt')
text_link_to_download_projecttraducaopt = translator.translate(text_link_to_download_project, dest='pt')
text_link_to_view_projecttraducaopt = translator.translate(text_link_to_view_project, dest='pt')
installationtraducaopt = translator.translate(installation, dest='pt')
python_explanationtraducaopt = translator.translate(python_explanation, dest='pt')
runningtraducaopt = translator.translate(running, dest='pt')
explicao_runningtraducaopt = translator.translate(explanation_running, dest='pt')
technologies_usedtraducaopt = translator.translate(technologies_used, dest='pt')
explanation_technologies_usedtraducaopt = translator.translate(explanation_technologies_used, dest='pt')
used_librarytraducaopt = translator.translate(used_library, dest='pt')
explanation_used_librarytraducaopt = translator.translate(explanation_used_library, dest='pt')
authortraducaopt = translator.translate(author, dest='pt')

#Japonese Translation
titulotraducaoja = translator.translate(title, dest='ja')
subtitulotraducaoja = translator.translate(subtitle, dest='ja')
altdaimagemtraducaoja = translator.translate(altimage, dest='ja')
text_link_to_download_projecttraducaoja = translator.translate(text_link_to_download_project, dest='ja')
text_link_to_view_projecttraducaoja = translator.translate(text_link_to_view_project, dest='ja')
installationtraducaoja = translator.translate(installation, dest='ja')
python_explanationtraducaoja = translator.translate(python_explanation, dest='ja')
runningtraducaoja = translator.translate(running, dest='ja')
explicao_runningtraducaoja = translator.translate(explanation_running, dest='ja')
technologies_usedtraducaoja = translator.translate(technologies_used, dest='ja')
explanation_technologies_usedtraducaoja = translator.translate(explanation_technologies_used, dest='ja')
used_librarytraducaoja = translator.translate(used_library, dest='ja')
explanation_used_librarytraducaoja = translator.translate(explanation_used_library, dest='ja')
authortraducaoja = translator.translate(author, dest='ja')

#Korean Translation
titulotraducaoko = translator.translate(title, dest='ko')
subtitulotraducaoko = translator.translate(subtitle, dest='ko')
altdaimagemtraducaoko = translator.translate(altimage, dest='ko')
text_link_to_download_projecttraducaoko = translator.translate(text_link_to_download_project, dest='ko')
text_link_to_view_projecttraducaoko = translator.translate(text_link_to_view_project, dest='ko')
installationtraducaoko = translator.translate(installation, dest='ko')
python_explanationtraducaoko = translator.translate(python_explanation, dest='ko')
runningtraducaoko = translator.translate(running, dest='ko')
explicao_runningtraducaoko = translator.translate(explanation_running, dest='ko')
technologies_usedtraducaoko = translator.translate(technologies_used, dest='ko')
explanation_technologies_usedtraducaoko = translator.translate(explanation_technologies_used, dest='ko')
used_librarytraducaoko = translator.translate(used_library, dest='ko')
explanation_used_librarytraducaoko = translator.translate(explanation_used_library, dest='ko')
authortraducaoko = translator.translate(author, dest='ko')

#Chinese Translation
titulotraducaozh_cn = translator.translate(title, dest='zh-cn')
subtitulotraducaozh_cn = translator.translate(subtitle, dest='zh-cn')
altdaimagemtraducaozh_cn = translator.translate(altimage, dest='zh-cn')
text_link_to_download_projecttraducaozh_cn = translator.translate(text_link_to_download_project, dest='zh-cn')
text_link_to_view_projecttraducaozh_cn = translator.translate(text_link_to_view_project, dest='zh-cn')
installationtraducaozh_cn = translator.translate(installation, dest='zh-cn')
python_explanationtraducaozh_cn = translator.translate(python_explanation, dest='zh-cn')
runningtraducaozh_cn = translator.translate(running, dest='zh-cn')
explicao_runningtraducaozh_cn = translator.translate(explanation_running, dest='zh-cn')
technologies_usedtraducaozh_cn = translator.translate(technologies_used, dest='zh-cn')
explanation_technologies_usedtraducaozh_cn = translator.translate(explanation_technologies_used, dest='zh-cn')
used_librarytraducaozh_cn = translator.translate(used_library, dest='zh-cn')
explanation_used_librarytraducaozh_cn = translator.translate(explanation_used_library, dest='zh-cn')
authortraducaozh_cn = translator.translate(author, dest='zh-cn')

#Chinese TW Translation
titulotraducaozh_tw = translator.translate(title, dest='zh-tw')
subtitulotraducaozh_tw = translator.translate(subtitle, dest='zh-tw')
altdaimagemtraducaozh_tw = translator.translate(altimage, dest='zh-tw')
text_link_to_download_projecttraducaozh_tw = translator.translate(text_link_to_download_project, dest='zh-tw')
text_link_to_view_projecttraducaozh_tw = translator.translate(text_link_to_view_project, dest='zh-tw')
installationtraducaozh_tw = translator.translate(installation, dest='zh-tw')
python_explanationtraducaozh_tw = translator.translate(python_explanation, dest='zh-tw')
runningtraducaozh_tw = translator.translate(running, dest='zh-tw')
explicao_runningtraducaozh_tw = translator.translate(explanation_running, dest='zh-tw')
technologies_usedtraducaozh_tw = translator.translate(technologies_used, dest='zh-tw')
explanation_technologies_usedtraducaozh_tw = translator.translate(explanation_technologies_used, dest='zh-tw')
used_librarytraducaozh_tw = translator.translate(used_library, dest='zh-tw')
explanation_used_librarytraducaozh_tw = translator.translate(explanation_used_library, dest='zh-tw')
authortraducaozh_tw = translator.translate(author, dest='zh-tw')

#Text Final
textopt = f"""<h1 align="center">
  {icon}<br>{titulotraducaopt.text}
</h1>

*Read this in other languages: [English](readme.md), [Portuguese](readme.pt.md), [한국어](readme.ko.md), [日本語](readme.ja.md), [简体中文](readme.zh-cn.md), [正體中文](readme.zh-tw.md).*: 

<h4 align="center">
  {subtitulotraducaopt.text}
</h4>

<p align="center"><img src="Images/preview.png" alt="{altdaimagemtraducaopt.text}"></p>

<h4 align="center"><a href="https://{linktoviewproject}">{text_link_to_view_projecttraducaopt.text}</a></h4>
<h4 align="center"><a href="https://github.com/{githubusername}/{linktodownloadproject}/archive/refs/heads/main.zip">{text_link_to_download_projecttraducaopt.text}</a></h4>

---

## {installationtraducaopt.text}
```
git clone https://github.com/{githubusername}/{linktodownloadproject}.git
```
```
pip install -r requirements.txt
```

```
{python_explanationtraducaopt.text}
```

## {runningtraducaopt.text}

```
{explicao_runningtraducaopt.text}
```

---

## 💼 {technologies_usedtraducaopt.text}
{explanation_technologies_usedtraducaopt.text}

- {technologies}

---

## 📚 {used_librarytraducaopt.text}
{explanation_used_librarytraducaopt.text}

- {libraries}

---

## 🦄 {authortraducaopt.text}<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/{githubusername}">
        <img src="{photoprofile}" width="100px;" alt="Photo of {githubnickname} on GitHub"/><br>
        <sub>
          <b>{githubnickname}</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---"""
textoen = f"""<h1 align="center">
  {icon}<br>{titulotraducaoen.text}
</h1>

*Read this in other languages: [English](readme.md), [Portuguese](readme.pt.md), [한국어](readme.ko.md), [日本語](readme.ja.md), [简体中文](readme.zh-cn.md), [正體中文](readme.zh-tw.md).*: 

<h4 align="center">
  {subtitulotraducaoen.text}
</h4>

<p align="center"><img src="Images/preview.png" alt="{altdaimagemtraducaoen.text}"></p>

<h4 align="center"><a href="https://{linktoviewproject}">{text_link_to_view_projecttraducaoen.text}</a></h4>
<h4 align="center"><a href="https://github.com/{githubusername}/{linktodownloadproject}/archive/refs/heads/main.zip">{text_link_to_download_projecttraducaoen.text}</a></h4>

---

## {installationtraducaoen.text}
```
git clone https://github.com/{githubusername}/{linktodownloadproject}.git
```
```
pip install -r requirements.txt
```

```
{python_explanationtraducaoen.text}
```

## {runningtraducaoen.text}

```
{explicao_runningtraducaoen.text}
```

---

## 💼 {technologies_usedtraducaoen.text}
{explanation_technologies_usedtraducaoen.text}

- {technologies}

---

## 📚 {used_librarytraducaoen.text}
{explanation_used_librarytraducaoen.text}

- {libraries}

---

## 🦄 {authortraducaoen.text}<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/{githubusername}">
        <img src="{photoprofile}" width="100px;" alt="Photo of {githubnickname} on GitHub"/><br>
        <sub>
          <b>{githubnickname}</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---"""
textoja = f"""<h1 align="center">
  {icon}<br>{titulotraducaoja.text}
</h1>

*Read this in other languages: [English](readme.md), [Portuguese](readme.pt.md), [한국어](readme.ko.md), [日本語](readme.ja.md), [简体中文](readme.zh-cn.md), [正體中文](readme.zh-tw.md).*

<h4 align="center">
  {subtitulotraducaoja.text}
</h4>

<p align="center"><img src="Images/preview.png" alt="{altdaimagemtraducaoja.text}"></p>

<h4 align="center"><a href="https://{linktoviewproject}">{text_link_to_view_projecttraducaoja.text}</a></h4>
<h4 align="center"><a href="https://github.com/{githubusername}/{linktodownloadproject}/archive/refs/heads/main.zip">{text_link_to_download_projecttraducaoja.text}</a></h4>

---

## {installationtraducaoja.text}
```
git clone https://github.com/{githubusername}/{linktodownloadproject}.git
```
```
pip install -r requirements.txt
```

```
{python_explanationtraducaoja.text}
```

## {runningtraducaoja.text}

```
{explicao_runningtraducaoja.text}
```

---

## 💼 {technologies_usedtraducaoja.text}
{explanation_technologies_usedtraducaoja.text}

- {technologies}

---

## 📚 {used_librarytraducaoja.text}
{explanation_used_librarytraducaoja.text}

- {libraries}

---

## 🦄 {authortraducaoja.text}<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/{githubusername}">
        <img src="{photoprofile}" width="100px;" alt="Photo of {githubnickname} on GitHub"/><br>
        <sub>
          <b>{githubnickname}</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---"""
textoko = f"""<h1 align="center">
  {icon}<br>{titulotraducaoko.text}
</h1>

*Read this in other languages: [English](readme.md), [Portuguese](readme.pt.md), [한국어](readme.ko.md), [日本語](readme.ja.md), [简体中文](readme.zh-cn.md), [正體中文](readme.zh-tw.md).*: 

<h4 align="center">
  {subtitulotraducaoko.text}
</h4>

<p align="center"><img src="Images/preview.png" alt="{altdaimagemtraducaoko.text}"></p>

<h4 align="center"><a href="https://{linktoviewproject}">{text_link_to_view_projecttraducaoko.text}</a></h4>
<h4 align="center"><a href="https://github.com/{githubusername}/{linktodownloadproject}/archive/refs/heads/main.zip">{text_link_to_download_projecttraducaoko.text}</a></h4>

---

## {installationtraducaoko.text}
```
git clone https://github.com/{githubusername}/{linktodownloadproject}.git
```
```
pip install -r requirements.txt
```

```
{python_explanationtraducaoko.text}
```

## {runningtraducaoko.text}

```
{explicao_runningtraducaoko.text}
```

---

## 💼 {technologies_usedtraducaoko.text}
{explanation_technologies_usedtraducaoko.text}

- {technologies}

---

## 📚 {used_librarytraducaoko.text}
{explanation_used_librarytraducaoko.text}

- {libraries}

---

## 🦄 {authortraducaoko.text}<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/{githubusername}">
        <img src="{photoprofile}" width="100px;" alt="Photo of {githubnickname} on GitHub"/><br>
        <sub>
          <b>{githubnickname}</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---"""
textozh_cn = f"""<h1 align="center">
  {icon}<br>{titulotraducaozh_cn.text}
</h1>

*Read this in other languages: [English](readme.md), [Portuguese](readme.pt.md), [한국어](readme.ko.md), [日本語](readme.ja.md), [简体中文](readme.zh-cn.md), [正體中文](readme.zh-tw.md).*: 

<h4 align="center">
  {subtitulotraducaozh_cn.text}
</h4>

<p align="center"><img src="Images/preview.png" alt="{altdaimagemtraducaozh_cn.text}"></p>

<h4 align="center"><a href="https://{linktoviewproject}">{text_link_to_view_projecttraducaozh_cn.text}</a></h4>
<h4 align="center"><a href="https://github.com/{githubusername}/{linktodownloadproject}/archive/refs/heads/main.zip">{text_link_to_download_projecttraducaozh_cn.text}</a></h4>

---

## {installationtraducaozh_cn.text}
```
git clone https://github.com/{githubusername}/{linktodownloadproject}.git
```
```
pip install -r requirements.txt
```

```
{python_explanationtraducaozh_cn.text}
```

## {runningtraducaozh_cn.text}

```
{explicao_runningtraducaozh_cn.text}
```

---

## 💼 {technologies_usedtraducaozh_cn.text}
{explanation_technologies_usedtraducaozh_cn.text}

- {technologies}

---

## 📚 {used_librarytraducaozh_cn.text}
{explanation_used_librarytraducaozh_cn.text}

- {libraries}

---

## 🦄 {authortraducaozh_cn.text}<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/{githubusername}">
        <img src="{photoprofile}" width="100px;" alt="Photo of {githubnickname} on GitHub"/><br>
        <sub>
          <b>{githubnickname}</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---"""
textozh_tw = f"""<h1 align="center">
  {icon}<br>{titulotraducaozh_tw.text}
</h1>

*Read this in other languages: [English](readme.md), [Portuguese](readme.pt.md), [한국어](readme.ko.md), [日本語](readme.ja.md), [简体中文](readme.zh-cn.md), [正體中文](readme.zh-tw.md).*: 

<h4 align="center">
  {subtitulotraducaozh_tw.text}
</h4>

<p align="center"><img src="Images/preview.png" alt="{altdaimagemtraducaozh_tw.text}"></p>

<h4 align="center"><a href="https://{linktoviewproject}">{text_link_to_view_projecttraducaozh_tw.text}</a></h4>
<h4 align="center"><a href="https://github.com/{githubusername}/{linktodownloadproject}/archive/refs/heads/main.zip">{text_link_to_download_projecttraducaozh_tw.text}</a></h4>

---

## {installationtraducaozh_tw.text}
```
git clone https://github.com/{githubusername}/{linktodownloadproject}.git
```
```
pip install -r requirements.txt
```

```
{python_explanationtraducaozh_tw.text}
```

## {runningtraducaozh_tw.text}

```
{explicao_runningtraducaozh_tw.text}
```

---

## 💼 {technologies_usedtraducaozh_tw.text}
{explanation_technologies_usedtraducaozh_tw.text}

- {technologies}

---

## 📚 {used_librarytraducaozh_tw.text}
{explanation_used_librarytraducaozh_tw.text}

- {libraries}

---

## 🦄 {authortraducaozh_tw.text}<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/{githubusername}">
        <img src="{photoprofile}" width="100px;" alt="Photo of {githubnickname} on GitHub"/><br>
        <sub>
          <b>{githubnickname}</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---"""

#Printing
with open('readme.md', 'w') as f:
    f.write(textoen)
    f.write('\n')
    print(Fore.GREEN + 'English ✔')
with open('readme.pt.md', 'w') as f:
    f.write(textopt)
    f.write('\n')
    print(Fore.GREEN + 'Portuguese ✔')
with open('readme.ja.md', 'w') as f:
    f.write(textoja)
    f.write('\n')
    print(Fore.GREEN + 'Japonese ✔')
with open('readme.ko.md', 'w') as f:
    f.write(textoko)
    f.write('\n')
    print(Fore.GREEN + 'Korean ✔')
with open('readme.zh-cn.md', 'w') as f:
    f.write(textozh_cn)
    f.write('\n')
    print(Fore.GREEN + 'Chinese ✔')
with open('readme.zh-tw.md', 'w') as f:
    f.write(textozh_tw)
    f.write('\n')
    print(Fore.GREEN + 'Chinese T ✔')