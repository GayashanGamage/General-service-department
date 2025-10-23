from playwright.sync_api import sync_playwright
import time
# from playwright.async_api import async_playwright
# from email_validator import validate_email, EmailNotValidError

class amazonProductsearch:

    def __init__(self):
        self.price = 0
        self.title = ''
        self.searchQuery = ''
        self.userEmail = 'gayashan.randimagamage@gmail.com'
        self.userPassword = '26efoi'
        self.availableBrowserList = []

        self.browser = ''
        self.context = ''
        self.tab_one = ''
        self.checkBrowserAvailability()

    def checkBrowserAvailability(self):
        """
        check what are the browsers available with the playwright environment
        return : none
        """
        browser_name_list = ['chromium','firefox', 'webkit']

        print("checking available browsers ....")
        for item in browser_name_list:
            try:
                with sync_playwright() as p:
                    self.browser = getattr(p, item).launch()
                    self.availableBrowserList.append(item)
                    self.browser.close()
                    print(f"{item} is working")
            except Exception:
                print(f"{item} is NOT installed or not working!")
        
        if len(self.availableBrowserList)  == 0:
            print('sorry! there is no any broser found. try to intall it and loach the program again')
        else:
            self.launchBrowser()

    def launchBrowser(self):
        """
        launch the web browser + new tab with open amazon.com website on it
        return : none
        """
        try:
            with sync_playwright() as p:
                print('this is try to execute')
                for item in self.availableBrowserList:
                    self.browser = getattr(p, item) .launch()
                    self.context = self.browser.new_context()
                    self.tab_one = self.context.new_page()

                    self.tab_one.goto('https://www.amazon.com/')
                    self.tab_one.wait_for_load_state('domcontentloaded')
                    
                    if self.tab_one.get_by_role("button", name="Continue shopping").is_visible():
                        self.tab_one.get_by_role("button", name="Continue shopping").click()
                        print(f'Amazon.com loaded in to {item} browser')
                        print(self.tab_one.title())
                        self.directToLogin()
                        break

                    elif self.tab_one.title().strip() == 'Amazon.com. Spend less. Smile more.':
                        print(f'Amazon.com loaded in to {item} browser')
                        print(self.tab_one.title())
                        self.directToLogin()
                        break
        except: 
            print('any browser cannot load amazon.com - check it manually from your browser.')

    def directToLogin(self):
        """
        click action to login page
        return : none
        """
        self.tab_one.get_by_role("link", name="Hello, sign in Account & Lists").click()
        self.chooseCredencialOptions()

    def chooseCredencialOptions(self):
        """
        ask user whether he go with the default user credencials or enter his amazon.com credencials to continue this program
        return : none
        """
        userChoise = input("Do you want to go with default credencials ? (Y/n)")
        if userChoise == 'Y':
            self.logInToSystem()
        elif userChoise == 'n':
            self.askEmail()
        else:
            print('Enter valied input.')
            self.chooseCredencialOptions()
    
    def askEmail(self):
        """
        if user decide to go with his credencials, ask what is the email / phone number that use for login to amazon.com
        return : none
        """
        self.userEmail = input('Enter your amazon account email or mobile number : ')
        self.tab_one.get_by_role("textbox", name="Enter your mobile number or").fill(self.userEmail)
        self.tab_one.get_by_role("button", name="Continue").click()
        self.tab_one.wait_for_load_state('domcontentloaded')
        self.checkAccountIsAvailable()

    def checkAccountIsAvailable(self):
        """
        if user decide ot go with his credencials, check entered email / phone number register under the amazon.com
        return : none
        """
        if self.tab_one.get_by_role("textbox", name="Password").is_visible():
            self.checkUserPassword()
        elif self.tab_one.get_by_role("heading", name="Looks like you're new to").is_visible():
            print('there is no amazon account under this email. enter correct one')
            self.tab_one.go_back()
            self.askEmail()

    def checkUserPassword(self):
        """
        if user decide ot go with his credencials, check entered password is mach with email
        return : none
        """
        self.userPassword = input('Enter your password : ')
        self.tab_one.get_by_role("textbox", name="Password").fill(self.userPassword)
        self.tab_one.get_by_role("button", name="Sign in").click()
        self.tab_one.wait_for_load_state('domcontentloaded')
        time.sleep(4)
        if self.tab_one.get_by_role("heading", name="There was a problem").is_visible():
            print('your password is incorrect. re try again')            
            self.tab_one.go_back()
            self.tab_one.wait_for_load_state('domcontentloaded')
            self.checkUserPassword()
        elif self.tab_one.title().strip() == 'Amazon.com. Spend less. Smile more.':
            print('now you can search products')
            self.searchProduct()



    def searchProduct(self):
        """
        check users preffered items price on amazon.com
        return : none
        """
        self.searchQuery = input('what you want to search ? ')
        self.tab_one.wait_for_load_state('domcontentloaded')
        self.tab_one.get_by_role("searchbox", name="Search Amazon").fill(self.searchQuery)
        self.tab_one.get_by_role("button", name="Go", exact=True).click()
        self.tab_one.wait_for_load_state('domcontentloaded')
        self.showProductDetails()


    def showProductDetails(self):
        """
        if that product is available, then get the name and price of the product
        return : none
        """
        self.tab_one.wait_for_load_state('domcontentloaded')
        self.tab_one.wait_for_selector('.s-result-item')
         
        self.tab_one.wait_for_load_state('domcontentloaded')
        product_prices = self.tab_one.locator('.a-size-base-plus').all()
        for title in product_prices[:1]:
            print("Title:", title.text_content())

        self.tab_one.wait_for_load_state('domcontentloaded')
        product_prices = self.tab_one.locator('.a-price .a-offscreen').all()
        for price in product_prices[:1]:
            print("Price:", price.text_content())
        self.searchProduct()
        

amazonProductsearch()



