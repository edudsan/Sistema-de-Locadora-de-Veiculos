# 🚗📋 Backlog do Produto - Sistema de Gestão de Locadora

## 📖 Introdução

Este backlog foi elaborado com base nas regras de negócio e necessidades de uma empresa de locação de veículos. O objetivo é gerenciar de forma eficiente o cadastro de **clientes**, a **frota de veículos** e o **ciclo de vida completo das reservas**. A estrutura foi pensada para garantir **clareza**, **priorização** e **rastreabilidade** das funcionalidades implementadas e futuras.

## 🛠️ Metodologia

O backlog foi dividido em **Épicos**, **Features** e **Histórias de Usuário**, com cada história associada a uma priorização definida com base no impacto da funcionalidade para o negócio.

<center>

<table border="1" style="border-collapse: collapse; width: 100%; text-align: center;">
  <caption style="caption-side: bottom; font-size: 0.9em; padding-top: 5px;">
    Fonte: <a href="https://github.com/edudsan">Eduardo Santos</a>
  </caption>
  <thead>
    <tr>
      <th style="padding: 8px;">Épico</th>
      <th style="padding: 8px;">Feature</th>
      <th style="padding: 8px;">História de usuário</th>
      <th style="padding: 8px;">Priorização</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6" style="padding: 8px;"><b>Épico 1 - Gestão de Cadastros</b></td>
      <td rowspan="3" style="padding: 8px;"><b>Feature 1 - Clientes</b></td>
      <td style="text-align: left; padding: 8px;"><b>US01</b> - Adicionar novo cliente (Pessoa Física ou Jurídica)</td>
      <td style="padding: 8px;">Alta</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 8px;"><b>US02</b> - Editar dados de um cliente existente</td>
      <td style="padding: 8px;">Média</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 8px;"><b>US03</b> - Apagar o registro de um cliente</td>
      <td style="padding: 8px;">Média</td>
    </tr>
    <tr>
      <td rowspan="3" style="padding: 8px;"><b>Feature 2 - Frota</b></td>
      <td style="text-align: left; padding: 8px;"><b>US04</b> - Adicionar novo veículo à frota</td>
      <td style="padding: 8px;">Alta</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 8px;"><b>US05</b> - Editar informações de um veículo</td>
      <td style="padding: 8px;">Média</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 8px;"><b>US06</b> - Excluir um veículo da frota</td>
      <td style="padding: 8px;">Média</td>
    </tr>
    <tr>
      <td rowspan="3" style="padding: 8px;"><b>Épico 2 - Operação da Locadora</b></td>
      <td rowspan="3" style="padding: 8px;"><b>Feature 3 - Reservas</b></td>
      <td style="text-align: left; padding: 8px;"><b>US07</b> - Adicionar uma nova reserva para um cliente</td>
      <td style="padding: 8px;">Alta</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 8px;"><b>US08</b> - Editar uma reserva existente</td>
      <td style="padding: 8px;">Alta</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 8px;"><b>US09</b> - Deletar/Cancelar uma reserva</td>
      <td style="padding: 8px;">Média</td>
    </tr>
    <tr>
      <td rowspan="2" style="padding: 8px;"><b>Épico 3 - Ferramentas e Relatórios</b></td>
      <td style="padding: 8px;"><b>Feature 4 - Consulta</b></td>
      <td style="text-align: left; padding: 8px;"><b>US10</b> - Buscar veículos disponíveis por período</td>
      <td style="padding: 8px;">Alta</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><b>Feature 5 - Relatórios</b></td>
      <td style="text-align: left; padding: 8px;"><b>US11</b> - Gerar relatório de faturamento por período</td>
      <td style="padding: 8px;">Alta</td>
    </tr>
  </tbody>
</table>

</center>

## 🗂️ Temas

As funcionalidades foram agrupadas em:

* 📌 **Gestão de Cadastros**: Recursos essenciais para o registro e manutenção das entidades principais do sistema (**clientes** e **veículos**).
* ⚙️ **Operação e Gestão**: Funcionalidades do dia a dia da locadora e ferramentas de apoio à tomada de decisão.

## 🏆 Épicos e Perfis



### 🧾 Épico 1 - Gestão de Cadastros

Permite estruturar os dados fundamentais do sistema, como **clientes** e **veículos**, que são a base para todas as outras operações.

<center>
🙋‍♂️ Como atendente/gerente, desejo poder cadastrar, editar e remover clientes e veículos para manter a base de dados da locadora organizada e atualizada.
</center>

---

### 🚗 Épico 2 - Operação da Locadora

Engloba toda a lógica central do negócio: o processo de **alugar um carro**. Isso inclui criar uma **reserva**, poder alterá-la conforme a necessidade do cliente e cancelá-la.

<center>
🙋‍♀️ Como atendente, desejo gerenciar o ciclo de vida completo de uma reserva para atender às solicitações dos clientes de forma eficiente.
</center>

---

### 📊 Épico 3 - Ferramentas e Relatórios

Agrupa funcionalidades que apoiam as operações diárias e a visão estratégica do negócio, permitindo **consultas inteligentes** e a **extração de dados financeiros**.

<center>
🧑‍💼 Como atendente e gerente, desejo ter ferramentas que me ajudem a encontrar veículos para os clientes e a entender a performance financeira da empresa.
</center>
