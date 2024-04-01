# CookieMonster

Cookie Monster is an automated authentication and cookie/storage changer, to test different cookie manipulation based security flaws. The tool is written in **python** using **selenium**.

## Library Dependencies

selenium, time, maskpass, pyfiglet

## Usage

Add your own webdriver path here.

```
driver = webdriver.Firefox(executable_path="")
```

Change the ID, TAGs.
Change the 'user' to your desired cookie or storage name.

```
driver.execute_script('''localStorage.removeItem("user");''')
```

Add your changed cookie or local storage value.

```
driver.execute_script('''
                            # Desired Changed Local Storage value.
                            # localStorage.setItem("user","")

                            ''')
```
