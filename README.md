# Gerador de logs

## Aplicação de Geração de Logs

Este projeto em flask é uma aplicação simples para geração de logs 
de teste para ambientes de monitoramento. Ele possui uma interface
simples feita para gerar registros de eventos e informações que
podem ser utilizadas para testar ferramentas de 
monitoração como Prometheus, Grafana Loki e outros.

## Utilização

Acesso o diretório principal onde encontra-se o arquivo **compose.yml** e execute o comando
 **docker compose build** para criação do container, em seguida execute o comando **docker compose up**
 e a aplicação será executada e estará disponível na porta 5000.

Os logs gerados são gravados em um arquivo chamado **logs.log** e também são exibidos no terminal, 
dessa forma você pode ler os logs diretamente do container ou através do arquivo de logs gerado. 