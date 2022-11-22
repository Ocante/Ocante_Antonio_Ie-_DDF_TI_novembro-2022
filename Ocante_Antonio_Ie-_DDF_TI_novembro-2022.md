\# Ocante\_Antonio\_Ie-\_DDF\_TI\_novembro-2022

\*\*Case\_Técnico\_da\_empresa\_Dadosfera\_(anteriormente\_DataSprints)\_referente\_à\_vaga\_Pessoa\_Analista\_de\_Tecnologia\_da\_Informação\_Júnior\*\*

Case 1: 4. Quais são alguns estilos de arquitetura para criar uma API da Web?

Resposta - 1 - Os 4 estilos de APIs mais utilizados e comentados atualmente no mercado são:

Web Service -

Também conhecido como Tunneling Style, é o padrão de mensagens Simple Object Access Protocol (SOAP). Por sua vez,  define uma interface Remote Procedure Call (RPC) para integração de aplicações e utiliza Web Services Description Language (WSDL) para o desenho das interfaces. Tem sua origem no mundo SOA, onde foram (e são ainda!) muito utilizadas para integração de redes.

Pragmatic REST

O estilo Representational State Transfer (REST) - utiliza Uniform Resource Identifier (URI) e uma abordagem Web-Centric para o desenho de interfaces suportando exclusivamente o protocolo HTTP. Sua linguagem é intuitiva e bem familiar a quem desenvolve para o ambiente mobile. Outra vantagem é que os dados podem ser armazenados nos clients prevenindo múltiplas chamadas. Além disso, pode retornar dados em múltiplos formatos (JSON, XML, etc...).

Hypermedia

Hypertext é um texto escrito em um formato estruturado que contém relacionamentos com outros objetos através de links. Hypermedia, além de texto,  compreende também imagens, vídeo, áudio e links e funciona de forma semelhante a uma página Web, fornecendo ao usuário orientações sobre o tipo de conteúdo que pode recuperar ou que ações eles podem realizar, permitindo dessa forma, explorar com mais ênfase todo o poder e a escalabilidade da Web.

Event-Driven

Esse estilo de API, permite a criação de aplicações mais dinâmicas e que necessitam de interfaces mais leves, é eficaz para aplicações que necessitam de um grande número de mensagens passando entre o servidor e o aplicativo, tais como os aplicativos de instant messaging e os famosos widgets, ou para aplicações com características bi-direcionais, como os jogos de vídeo game multiplayer.

Case 2: Escreva um script, em Shell ou Power Shell ou Python, que consulta uma lista de usuários e

e-mails num CSV chamado “users\_emails”. Para cada e-mail, cria um usuário, no Windows ou Linux,

de sua máquina local. Explique o que cada chamada dos scripts faz.

Resposta:

\-----------------------------------------------------------------------------------------------------------------------

import pandas as pd

import numpy as np

import string

import random

from unidecode import unidecode

import subprocess as sub


def password\_generator(tam=10):

password = ""

chars = [string.ascii\_letters, string.punctuation, string.digits]

for i in range(tam):

charTypeValue = np.random.choice([0, 1, 2], p=[0.8, 0.1, 0.1])

charType = chars[charTypeValue]

password += random.choice(charType)

return password


def user\_generator(string):

return unidecode(string.lower().replace(' ', ''), 'uft-8')


dados = pd.read\_csv('user\_emails.csv', sep=';', header=None)

\# Bloco command:

\# 1) Adiciona o usuário da criado à variável newuser do Powershell

\# 2) Adiciona a senha da criado à variável newpassword do Powershell

\# 3) Cria um usuário local com o nome: newuser e senha:newpassword

\# 4) Adiciona esse usuáro ao Grupo correto do Windows

for person in dados.iloc[:, 0]:

user = user\_generator(person)  # Cria um usário a partir do nome e sobrenome

password = password\_generator()  # Cria uma senha aleatória de 10 digítos

command = """

$newuser = """ + f'"{user}"' """

$newpassword = ConvertTo-SecureString """ + f'"{password}"' + """ -AsPlainText -Force

New-LocalUser -Name $newuser -Password $newpassword

Add-LocalGroupMember -Group "Administrators" -Member $newuser

"""

print(command)

exec = sub.Popen(["powershell", "& {" + command + "}"])

\-----------------------------------------------------------------------------------------------------------------------


Case 3: Uma plataforma de gerenciamento de diretório em nuvem será implementada na empresa.

Considerando as features de MDM (master device management), SSO e user lifecycle, como poderia

ser organizado o projeto de implementação? E o gerenciamento/auditoria?

Resposta:

Para organizar o projeto de implementação e o gerenciamento/auditoria, primeiramente é necessário criar uma estratégia e um conjunto de metas, uma articulação de longo prazo, ter prioridades realistas, um orçamento e prazos claros. E em seguida iniciar com a definição de Custo de manutenção da Nuvem, % ganho operacional, número de vulnerabilidades de segurança identificadas.Levando em consideração as features de MDM (master device management) a estratégia de Migração deve se atentar a Economia em infraestrutura, número de incidentes por aplicação/infra/pessoas, tempo de reparo e tempo entre as falhas, tempo de deploy de infraestrutura. Quando se trata de  SSO e user lifecycle, vale sustentar a prática de otimização de percentagem de policies em compliance, tempo economizado como resultado de policies definidas, percentagem de disponibilidade de serviço contratado. É de extrema importancia o mapeamento da sua rede e identifique onde a nuvem se encaixa nela. Obtendo sempre a imagem clara do papel da nuvem em sua estratégia geral de gerenciamento de diretório. Saber qual o provedor do seu link Internet; a Tecnologia a ser utilizada (MPLS, Frame Relay); Número de circuito, telefone de suporte, SLA; Lista dos domínios que sua empresa registrou e qual a data de expiração; Servidores DNS e registros DNS existentes (A, Mx, etc)). Uma das definições importante e que pode ser considerada no gerenciamento e auditoría, logo na organização do projeto, é de suma importancia Documentação dos servidores, como nome do servidor, IP, finalidade, SO instalado, informações de hardware do servidor (processador, memória, disco, partições), serviços instalados, Documentação da instalação; Topologia de rede, Diagrama da topologia lógica, Diagrama de Vlans, Diagramas da topologia física, Estrutura da árvore LDAP (ou Active Directory, ser for o caso), Topologia do Storage, Layout do datacenter e dos racks Ativos de rede Roteadores (nome, IP, marca, modelo, localização) Switches (nome, IP, marca, modelo, localização), Firewalls (nome, IP, marca, modelo, localização). Contudo o esboço da parte técnica ser primordial, mas i mais impornte é a parte operacional, o investimento em treinamento dos funcionários para entender todo fluxo de projeto de implementação. O gerenciamento da nuvem pode ser simplificado se você usar a automação inteligente de processos para criar, implantar e monitorar seus recursos e aplicativos. Adote os princípios e práticas do DevOps para automatizar o gerenciamento de seus ambientes em nuvem. Essa é a forma basicamente de organizar o projeto de implementação da plataforma de gerenciamento de diretório agregando

as features, SSO e user lifecycle, e por sua vez facilitar o gerenciamento/auditoria.

Case 4: Quais são as estruturas de dados em Python?

Resposta: Principais Estruturas de Dados no Python são as Listas, Sets, Dicionários e Tuplas.

- Listas

Uma lista é a estrutura de dados mais básica do Python e armazena os dados em sequência, onde cada elemento possui sua posição na lista, denominada de índice. O primeiro elemento é sempre o índice zero e a cada elemento inserido na lista esse valor é incrementado. E pode armazenar qualquer tipo de dado como: Inteiro Ponto Flutuante ou Decimal, String, Boolean, List, Tuple, Dictionary.

- Tuplas

Uma tupla é uma estrutura bastante similar a uma lista, porém, posuí uma diferença: os elementos inseridos em uma tupla não podem ser alterados, diferente de uma lista onde podem ser alterados livremente

- Sets

Em Python, os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados. Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos e são utilizados, normalmente, com operações matemáticas de união, interseção e diferença simétrica.

- Dicionários

Em Python, os dicionários são coleções de itens desordenados com uma diferença bem grande quando comparados às outras coleções (lists, sets, tuples, etc): um elemento dentro de um dicionário possui uma chave atrelada a ele, uma espécie de identificador.

Case 5: Como você mediria a eficiência da nossa equipe de operações?

Resposta:

Para medir a eficiência operacional é necessário dividir a produção pela entrada (recursos, horas trabalhadas, pessoal, etc.). Vale resaltar que a eficiência está relacionada a produzir o mesmo resultado com menos recursos. Gestor(a) deve levar em consideração as variáveis de saída e entrada que condizem com a empresa. Há diversos indicadores que podem demonstrar o nível de entrega, motivação e comprometimento dos funcionários com o que é solicitado. É muito importante conhecer esses indicadores, bem como mensurá-los com periodicidade. Entre os principais, podemos destacar o número de reclamações dos clientes, o nível de absenteísmo, o índice de quebras, o refugo de materiais e o nível de produtividade. Essas variáveis são determinadas por meio de indicadores de desempenho. Eficiência operacional e desempenho do negócio não se resume apenas em produzir mais com os mesmos recursos. É ter a possibilidade de identificar em quais áreas existem “desperdícios” que podem ser facilmente eliminados para aumentar a eficiência.O gestor deve se concentrar em aproveitar ao máximo essas métricas para ir além de cortar custos, mas encontrar uma estratégia para entender como a organização opera e logo, será possível atuar com maior desempenho e extrair mais resultados.
