from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_multiple_elements():
    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument("--headers")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usade")

    driver = webdriver.Chrome(options=options)

    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9

    for link in links:
        assert link.is_displayed()

    assert "1" in links[0].text

    driver.quit()

test_multiple_elements()
