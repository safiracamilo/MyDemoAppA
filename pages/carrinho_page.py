from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

class CarrinhoPage(BasePage):
    #localizadores
    _icone_carrinho = {'by': AppiumBy.ACCESSIBILITY_ID,'value': "com.saucelabs.mydemoapp.android:id/cartTV"}  # o meu foi o el6
    _titulo_produto = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'com.saucelabs.mydemoapp.android:id/titleTV'}
    _preco_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
    _preco_total = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/totalPriceTV'}

    #inicializaçao
    def __int__(self,driver):
        self.driver = driver

    #ir para carrinho de compras
    def ir_para_o_carrinho_de_compras(self):
        self._apertar(self._icone_carrinho)

    #ler os dados do produto no carrinho
    def ler_dados_do_carrinho(self):
        dados = {}
        dados.titulo = self._ler(self._titulo_produto)
        dados.preco_produto = (self._preco_produto)
        dados.preco_total = (self._preco_total)
        return dados



