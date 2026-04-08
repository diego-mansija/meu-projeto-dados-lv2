Dashboard Interativo de Performance de Vendas

Este repositório expande as capacidades de análise do projeto anterior, introduzindo uma interface web dinâmica desenvolvida com Streamlit. O projeto migra de uma execução de scripts estáticos para uma aplicação de dados completa, permitindo a exploração de indicadores em tempo real com filtragem reativa.

1. Objetivo

Desenvolver uma interface de business intelligence que permita ao usuário final filtrar métricas de faturamento e volume de vendas de forma autônoma. A aplicação consolida indicadores-chave de desempenho (KPIs) e visualizações gráficas em um ambiente web acessível via navegador.

2.  Tecnologias e Ferramentas

    Ambiente de Desenvolvimento: Linux Mint.

    Linguagem: Python 3.12.

    Interface Web: Streamlit para o desenvolvimento do dashboard e widgets interativos.

    Processamento de Dados: Pandas para manipulação de DataFrames e agregação de métricas.

    Visualização: Matplotlib integrado ao contêiner do Streamlit.

    Deploy: Streamlit Community Cloud para hospedagem da aplicação.

3.  Estrutura de Diretórios

        meu-projeto-dados/
        ├── data/
        │   └── vendas.csv          # Base de dados estruturada
        ├── src/
        │   └── app.py              # Script principal da aplicação Streamlit
        ├── .streamlit/
        │   └── config.toml         # Configurações de tema e layout do dashboard
        ├── .gitignore              # Definição de arquivos ignorados (incluindo .venv)
        ├── README.md               # Documentação do projeto
        └── requirements.txt        # Dependências incluindo streamlit e pandas

4.  Funcionalidades Implementadas

    Painel de Métricas (KPIs): Visualização instantânea de Faturamento Total, Quantidade de Itens Vendidos e Ticket Médio.

    Filtros Dinâmicos: Barra lateral interativa que permite a segmentação dos dados por categoria de produto, atualizando todos os gráficos simultaneamente.

    Gráficos Reativos: Integração de gráficos que respondem aos inputs do usuário sem necessidade de recarregamento manual da página.

    Otimização de Performance: Implementação de recursos de cache (@st.cache_data) para otimizar a leitura da base de dados e reduzir o consumo de memória.

5.  Instruções de Instalação e Execução

5.1 Configuração do Ambiente

Clone o repositório:

    git clone https://github.com/diego-mansija/meu-projeto-dados-lv2.git

Criação e ativação do ambiente virtual:

    python3 -m venv .venv
    source .venv/bin/activate

Instalação das dependências:

    pip install -r requirements.txt

5.2 Execução da Aplicação

Para rodar o dashboard localmente no ambiente Linux Mint:

        streamlit run src/app.py

A aplicação terá como padrão o server http://localhost:8501.

6. Demonstração e Acesso Online

A aplicação está disponível para visualização pública através do link abaixo:

        [Acesse o Dashboard Online](https://meu-projeto-dados-lv2.streamlit.app/)
