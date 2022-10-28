# Convert

![Captura de tela de 2022-10-28 19-52-31](https://user-images.githubusercontent.com/96485637/198747749-cd704da5-82b1-47fc-a1df-6ae1a4fac63f.png)

O convert é um Script em python feito para rodar em terminais Linux por linhas de comnandos, onde tem o objetivo 
de fazer conversões de arquivos entre eles poderá ser trabalhado tipos como Docx para ODT, ODT para PDF, PDF para DocX.

* Python3 convert.py -h    <- Esse primeiro comando serve para mostrar uma lista com todas as opções para uso. 

![img1](https://user-images.githubusercontent.com/96485637/198747915-8fbe1e32-74b1-48b1-ad10-fc7cf73a6ea2.png)


* python covert.py -cf (Caminho do arquivo) <- Aqui convertemos PDF para DocX.


![img2](https://user-images.githubusercontent.com/96485637/198748079-a4056bcb-4b24-461e-a592-03324473124c.png)


Para realizar outra função basta substituir o -cf por outro parâmetro, caso o parâmetro como mostrado no exemplo. 

Caso o parâmetro seja inválido ele irá retornar uma negativa.

![img3](https://user-images.githubusercontent.com/96485637/198748205-82b34ed5-0fa3-4bd0-ad60-8f6b511f6eca.png)


# Requisitos

* Python 3.10
* sys 
* from pdf2docx import Converter (pip install pdf2docx)
* aspose.words (pip install aspose-words)
* Linux(Ubuntu ou Debian)

