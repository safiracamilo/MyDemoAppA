from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class InicialPage(BasePage):
    # Localizadores/locators
    _product_image_view = {'by': AppiumBy.ACCESSIBILITY_ID,
                           'value': 'Sauce Lab Back Packs'}  # primeiro elemento-primeira acao, clicou no primeiro produto

    # mapear os demais elementos da tela (foi mapeado apenas um produto)

    # inicializacao
    def __init__(self, driver):
        self.driver = driver
        self._iniciar()
        # poderia realizar um assert de algum elmento para validar se a tela certa

    # acoes
    def selecionar_primeiro_produto_(self):
        self._apertar(self._product_image_view)
