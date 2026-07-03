import language_tool_python
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
import os
import sys

def caminho_recurso(nome):
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, nome)
    return os.path.join(os.path.dirname(__file__), nome)

class Corretor:
    """Classe para o corretor de texto"""
    def __init__(self):

        carregador=QUiLoader()
        self.ui=carregador.load(caminho_recurso('interface_corretor_de_texto.ui'))

        #titulo do app
        self.ui.setWindowTitle('Corretor de Texto')
        self.ui.setWindowIcon(QIcon(caminho_recurso('icone.ico')))

        #Botão corrigir texto
        self.ui.botao_corrigir.clicked.connect(self.corretor_completo)

    def corretor_completo(self):

        #recebimento dos produtos de entrada -> texto de indicação=texto_indicador e texto corrigido=texto_dev_corrigido
        texto_indicador,texto_dev_corrigido=self.indicador_texto()

        #devolutiva do texto transcrito
        campo_indicador_texto = self.ui.saida_texto_indicador
        campo_texto_corrigido=self.ui.saida_texto_corrigido

        # A linha abaixo coloca o texto transcrito somente para modo leitura
        campo_indicador_texto.setReadOnly(True)
        campo_texto_corrigido.setReadOnly(True)

        campo_indicador_texto.setPlainText("\n".join(texto_indicador))
        campo_texto_corrigido.setPlainText(texto_dev_corrigido)

    def indicador_texto(self):

        # Coleto do texto do usuario e tradução
        self.texto_usuario = self.ui.entrada_texto_usuario.toPlainText()

        # Inicializa o corretor para o português do Brasil
        tool = language_tool_python.LanguageTool('pt-BR')

        # Encontra os erros
        erros = tool.check(self.texto_usuario)

        # Comentando os erros:
        list_strings_indicadores=[]
        for erro in erros:
            var_temp_txt=f"Erro encontrado: '{self.texto_usuario[erro.offset: erro.offset + erro.error_length]}'"
            list_strings_indicadores.append(var_temp_txt)
            var_temp_txt =f"Mensagem: {erro.message}"
            list_strings_indicadores.append(var_temp_txt)
            var_temp_txt =f"Sugestões: {erro.replacements[0]}"
            list_strings_indicadores.append(var_temp_txt)
            var_temp_txt ="-" * 42
            list_strings_indicadores.append(var_temp_txt)

        texto_corrigido = tool.correct(self.texto_usuario)

        return list_strings_indicadores,texto_corrigido

#Executor da interface
if __name__ == '__main__':
    aplicativo = QApplication()

    interfaces = Corretor()
    interfaces.ui.show()

    aplicativo.exec()