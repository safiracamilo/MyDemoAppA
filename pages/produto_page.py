from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class ProdutoPage(BasePage):
      # localizadores
      #wait = WebDriverWait(BasePage, 30)
      #_preco_produto = wait.until(By.Id, "com.saucelabs.mydemoapp.android:id/priceTV")
      #_nome_produto = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'com.saucelabs.mydemoapp.android:id/productTV'}
      #_preco_produto = {'by': AppiumBy.Id, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
      _nome_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/productTV'}
      _preco_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
      _origem_x =572
      _origem_y =309
      _destino_x =661
      _destino_y =296
      _origem_x = 505
      _origem_y = 422
      _destino_x = 532
      _destino_y= 392
      _origem_x = 462
      _origem_y = 362
      _destino_x = 226
      _destinoY = 169
      _color_image_viw = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'Gray color' } # o meu foi o el3
      _aumentar_quantidade = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'Increase item quantity'}  # o meu foi o el4
      _adicionar_carrinho = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'Tap to add product to cart'}  # o meu foi o el5



      def __int__(self, driver):
          self.driver = driver
          # poderia validar se abriu a tela correta (acrescentar no projeto)

      #acoes
      #validar o produto e o preco
      def validar_nome(self):
          return self._ler(self._nome_produto) #el2

      def validar_preco(self):
            return self._ler(self._preco_produto) #el7


      #continuar o fluxo de compra

      def arrastar_para_cima(self):
          self._rolar(
                self._origem_x,
                self._origem_y,
                self._destino_x,
                self._destino_y
          )

      def como_(self,quantidade):
      # selecionar a cor da mochila
        self._apertar(self._color_image_viw)

      # selecionar quantidade do produto

        # selecionar a quantidade do produto
        # como ja vem selecionado um produto, se for uma para comprar, nao e necessario
        # clicar no elmento. Se forem 2 produtos, clica uma vez, se forem 3, clica 2 vezes
        for iten in range(quantidade -1):
            self._apertar(self._aumentar_quantidade)

        #adicionar o produto no carrinho
        self._apertar(self._adicionar_carrinho)












