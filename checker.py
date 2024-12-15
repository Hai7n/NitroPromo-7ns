from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options

# Setup Proxy details
proxy_address = "proxy.have-a.vision:9009"
username = "swiftshop"
password = "rajvaibhav56"

# Create Chrome options
chrome_options = Options()

# Set up proxy with authentication
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_address
proxy.ssl_proxy = proxy_address

# Add proxy settings to the Chrome options
chrome_options.add_argument(f'--proxy-server=http://{username}:{password}@{proxy_address}')

# Set up WebDriver with the proxy settings
driver = webdriver.Chrome(options=chrome_options)

# Open a website (for example, Google)
driver.get('https://www.google.com')

# Wait a few seconds to observe the result
driver.implicitly_wait(5)

# Close the driver
driver.quit()


