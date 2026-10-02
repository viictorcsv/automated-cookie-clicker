# Cookie Clicker Bot - Selenium Automation

Este repositório contém um script de automação (bot) desenvolvido em Python para jogar **Cookie Clicker** automaticamente.

O principal objetivo deste projeto foi **treinar e aprimorar habilidades com a biblioteca Selenium**, explorando conceitos de manipulação de DOM, esperas explícitas (WebDriverWait) e contorno de detecção de bots.

## Sobre o Projeto

Este script não é apenas um auto-clicker simples. Ele utiliza técnicas avançadas de Web Scraping para interagir com o jogo de forma inteligente. Em vez de apenas clicar, ele analisa o estado do jogo para comprar as melhores atualizações e construções disponíveis, maximizando a produção de cookies.

### Tecnologias Utilizadas
* **Python 3.x**
* **Selenium WebDriver:** Para interação e controle do navegador.
* **Undetected Chromedriver:** Para evitar que o script seja bloqueado por verificações anti-bot (Cloudflare/Human Verification).

## Funcionalidades

* **Burlador de Detecção:** Utiliza uma instância modificada do Chrome para passar por verificações de segurança que bloqueiam o Selenium padrão.
* **Auto-Click de Alta Performance:** Realiza cliques rápidos no "Big Cookie" em lotes otimizados para não travar o script.
* **Compra Inteligente (Smart Buy):**
    * Identifica automaticamente quando um item pode ser comprado verificando a classe CSS `enabled`.
    * Não depende de leitura de texto (OCR ou conversão de string), evitando erros com números grandes (ex: "1.5 million").
* **Priorização de Investimentos:**
    * Verifica primeiro se há **Upgrades** disponíveis.
    * Em seguida, verifica as **Construções (Buildings)**, sempre priorizando as mais caras e eficientes (do final para o início da lista).
* **Tratamento de Erros:** Lida com elementos dinâmicos que aparecem/desaparecem (StaleElementReferenceException) sem interromper a execução.

## Instalação

Pré-requisitos: Você precisa ter o **Python** e o **Google Chrome** instalados na sua máquina.

1. Clone este repositório:
   ```bash
   git clone https://github.com/viictorcsv/automated-cookie-clicker.git
