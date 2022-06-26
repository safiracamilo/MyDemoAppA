import pytest
from appium.protocols import webdriver

from . import config, credentials

#vaionlores default
def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default= '@ondemand.eu-central-1.saucelabs.com:443/wd/hub',  #pega essa informacao no site do saucelbas
        help= 'local onde está o servidor Appium'
    )

    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='servidor local ou na nuvem'
    )

    parser.addoption(
        '--platform_name',
        action='store',
        default='Android',
        help='Sistema Operacional do dispositovo ou emulador'
    )

    parser.addoption(
        '--plalform_version',
        action='store',
        default='9.0',
        help='Versão do Sistema Operacional do dispositov ou emulador'
    )

@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.host = request.config.getoption('--host')
    config.platform_name = request.config.getoption('--platform_name')
    config.platform_version = request.config.getoption('--platform_version')

    # direciona para a execucao no saucelabs ou local
    if config.host == 'saucelabs':
        test_name = request.node.name # nome do teste
        caps = {
            "platformName": config.platform_name,
            "appium:plafformVersion": config.platform_version,
            "appium:deviceName": "Samsung Galaxy S9 FHD GoogleAPI Emulador",
            "appium:deviceOrientation": "portrait",
            "appium:app": "storage:filename=mda-1.0.13-15.apk",
            "appium:appPackage": "com.saucelabs.mydemoapp.android",
            "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActiivity",
            "sauce:options": {
                 'name': test_name  #nome do teste
            }
    }
        # montar a credencial e a url
        _credentials = credentials.SAUCE_USERNAME + credentials.SAUCE_ACCESS_KEY
        _url = 'https://' + _credentials + config.baseurl

        # instaciar o Saucelabs

        driver_ = webdriver.Remote(_url, caps)

        # execucao local
    else:
        caps = {
            "platformName": config.platform_name,
            "appium:plafformVersion": config.platform_version,
            "appium:appiumVersion": "1.22.3",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "emulador5554",
            "appium:deviceOrientation": "portrait",
            "appium:appPackage": "com.saucelabs.mydemoapp.android",
            "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActiivity"
        }
        driver_ = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    #funcao de finalizacao
    def quit():
        sauce_result = 'failed' if request.node.rep_call.failed else 'passed'
        driver_.execute_scripit('sauce:job-result={}'.format(sauce_result))
        driver_.quit()
    request.addfinalizar(quit)
    return driver_


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makerpory(item,call):
    outcome= yield
    rep = outcome.get_result()
    setattr(item,'rep_' + rep.when,rep)