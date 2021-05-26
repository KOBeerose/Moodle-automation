# Moodle-automation
This a Python program I created to automate the reapeted task of checking the our school's time table, signing in to Moodle platform entring the current course and the joining the online room.


> **_NOTE:_**  Selenium Tools are required to run this script.

---


# Selenium Tools for Microsoft Edge

Selenium Tools for Microsoft Edge extends [Selenium 3](https://www.selenium.dev/) with a unified driver to help you write automated tests for both the Microsoft Edge (EdgeHTML) and new Microsoft Edge (Chromium) browsers.

The libraries included in this project are fully compatible with Selenium's built-in Edge libraries, and run Microsoft Edge (EdgeHTML) by default so you can use our project as a seamless drop-in replacement. In addition to being compatible with your existing Selenium tests, Selenium Tools for Microsoft Edge gives you the ability to drive the new Microsoft Edge (Chromium) browser and unlock all of the latest functionality!

The classes in this package are based on the existing ``Edge`` and ``Chrome`` driver classes included in the [Selenium](https://github.com/SeleniumHQ/selenium) project.


## Getting Started

### Downloading Driver Executables

You will need the correct [WebDriver executable](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for the version of Microsoft Edge you want to drive. The executables are not included with this package. WebDriver executables for all supported versions of Microsoft Edge are available for download [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). For more information, and instructions on downloading the correct driver for your browser, see the [Microsoft Edge WebDriver documentation](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp).

### Installation

```
pip install msedge-selenium-tools selenium==3.141
```

## Example Code


```py
from msedge.selenium_tools import Edge, EdgeOptions

# Launch Microsoft Edge (EdgeHTML)
driver = Edge()

# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options = options)
```

