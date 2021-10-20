from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class AbsenAutomation:
    def __init__(self, baseUrl: str):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.baseUrl = baseUrl
        self.emailS = 'input[autocomplete=email]'
        self.emailV = 'gorengmbah@gmail.com'
        self.nameS = 'input[aria-labelledby=i7]'
        self.nameV = 'Rendi Saputra'
        self.radioS = '.docssharedWizToggleLabeledLabelWrapper'
        self.nisS = 'input[aria-labelledby=i11]'
        self.nisV = '20439'

    def start(self):
        self.browser.get(self.baseUrl)
        self.inputContent()

    def inputContent(self):
        self.inputs(self.emailS)[0].send_keys(self.emailV)
        self.inputs(self.nameS)[0].send_keys(self.nameV)
        self.inputs(self.nisS)[0].send_keys(self.nisV)
        checkbox = self.inputs(self.radioS)
        checkbox[0].click()
        checkbox[3].click()

        self.inputs('.appsMaterialWizButtonPaperbuttonContent')[0].click()

        self.inputs('div[jsname=M2UYVd]')[0].click()

        time.sleep(60)

    def inputs(self, selector):
        return self.browser.find_elements_by_css_selector(selector)
