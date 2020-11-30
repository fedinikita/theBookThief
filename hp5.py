from selenium import webdriver
import time

def main():
    driver = webdriver.Chrome()
    for i in range(240, 367):
        driver.get(f'https://kniga.zone/read/{i}/?book=8845&font=Helvetica&size=15')
        time.sleep(0.25)
        parse = driver.find_element_by_id('bookread').text

        with open("test.txt", "a", encoding='utf-8') as file:
            file.write("%s\n" % parse)
        print(i)

if __name__ == '__main__':
    main()