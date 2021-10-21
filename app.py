from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class AbsenAutomation:

    data = {
        'esel': 'input[autocomplete=email]',
        'eval': 'gorengmbah@gmail.com',
        'nsel': 'input[aria-labelledby=i7]',
        'nval': 'Rendi Saputra',
        'nisel': 'input[aria-labelledby=i11]',
        'nival': '20439'
    }

    def __init__(self, baseUrl: str):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.baseUrl = baseUrl
        self.radioS = '.docssharedWizToggleLabeledLabelWrapper'

    def start(self):
        self.browser.get(self.baseUrl)
        self.inputContent()
        time.sleep(60)

    def inputContent(self):
        self.baseInput()
        self.checkBoxInput()
        self.buttonClick()

    def baseInput(self):
        self.inputs(self.data['esel'])[0].send_keys(self.data['eval'])
        time.sleep(30)
        self.inputs(self.data['nsel'])[0].send_keys(self.data['nval'])
        time.sleep(20)
        self.inputs(self.data['nisel'])[0].send_keys(self.data['nival'])
        time.sleep(40)

    def checkBoxInput(self):
        checkbox = self.inputs(self.radioS)
        time.sleep(20)
        checkbox[0].click()
        time.sleep(20)
        checkbox[3].click()

    def buttonClick(self):
        time.sleep(20)
        self.inputs('.appsMaterialWizButtonPaperbuttonContent')[0].click()
        time.sleep(40)
        self.inputs('div[jsname=M2UYVd]')[0].click()

    def inputs(self, selector):
        return self.browser.find_elements_by_css_selector(selector)
