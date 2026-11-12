# Trabalho final — Computação em Nuvem
## Projeto: Esteira completa de CI/CD para uma API na AWS

**Duração:** 2 semanas (14 dias corridos a partir da disponibilização). **Equipe:** individual, dupla ou trio. **Valor sugerido:** 100 pontos.

### Contextualização
Uma equipe recebeu uma API Python que funciona localmente, mas precisa transformá-la em serviço acessível em nuvem, com testes automatizados, empacotamento em contêiner e publicação automática a cada integração aprovada. O repositório-base é fornecido pelo professor. Não é necessário criar toda a API do zero: o objeto principal do trabalho é **a esteira de entrega e a infraestrutura de nuvem**.

### Objetivo
Configurar e demonstrar todo o fluxo: desenvolver em branch, abrir Pull Request, executar CI no GitHub Actions, integrar na `main`, publicar imagem no GitHub Container Registry e executar CD automatizado em instância AWS EC2, validando HTTP `/health`.

### Requisitos obrigatórios
1. Repositório próprio criado a partir da base, com README contendo os integrantes e instruções de uso.
2. Instância EC2 Linux com Docker funcional, Security Group documentado e aplicação acessível via HTTP.
3. CI em GitHub Actions: instalar dependências, executar `pytest`, realizar build Docker; PR não pode publicar imagem nem disparar deploy.
4. Publicação de imagem versionada por **SHA do commit**, no GHCR, somente quando mudanças entram em `main`.
5. CD em Actions, condicionado ao sucesso da CI, implantando na EC2 a imagem correspondente ao commit e checando `/health`.
6. Secrets/variables configurados sem expor credenciais ou chaves no código, logs ou README; acesso SSH restrito, conforme guia fornecido.
7. Implementar `DELETE /tasks/<id>` com retorno HTTP 204/404 e no mínimo 2 testes; implementar mais 1 melhoria e teste.
8. Pelo menos 1 branch `feature/...`, 1 PR com revisão (própria no trabalho individual), CI aprovada e merge na `main`.
9. Demonstrar que os dados persistem após recriação do contêiner.
10. Encerrar recursos utilizados para evitar cobranças; apresentar evidências.

### Cronograma sugerido
- **Dias 1–3:** compreender API, clonar/criar repositório, rodar testes e Docker local.
- **Dias 4–5:** configurar EC2, rede, Docker, criar endpoints e testes.
- **Dias 6–7:** abrir PR e comprovar execução da CI.
- **Dias 8–10:** configurar GHCR, segredos e CD; realizar primeiro deploy.
- **Dias 11–12:** corrigir problemas, demonstrar nova versão, persistência e checagem `/health`.
- **Dias 13–14:** documentação, apresentação, evidências e limpeza de recursos.

### Entrega
Enviar no Moodle: URL do repositório GitHub (conceder acesso ao professor, se privado), URL ou IP da aplicação enquanto estiver disponível, link do PR, links de ao menos um run de CI e um de CD aprovados, README atualizado, relatório curto (máximo 4 páginas ou Markdown no repositório) com diagrama, infraestrutura/portas, registro dos custos/recursos, dificuldades e evidências da persistência. Inserir integrantes e distribuição das tarefas. Vídeo de 3–5 minutos ou demonstração de até 5 minutos com PR/Actions/API funcionando, a critério do docente.

### Avaliação (100 pontos)
| Critério | Pontos |
|---|---:|
| Git/branches/PR e organização do repositório | 10 |
| Testes e CI funcionando nos PRs | 20 |
| Docker e publicação versionada no GHCR | 15 |
| Infraestrutura EC2, rede e segurança | 15 |
| CD automático e verificação de saúde | 20 |
| Evolução funcional com testes | 10 |
| Documentação, evidências e apresentação | 10 |

**Regras:** os mesmos critérios valem para grupos de 1, 2 ou 3 participantes. Todos devem saber explicar suas contribuições. É proibido versionar chaves privadas, tokens ou dados reais. Não utilizar `0.0.0.0/0` no acesso SSH; o professor deverá orientar uma solução segura para os runners de deploy. O funcionamento fora do horário da apresentação não é obrigatório após o encerramento da infraestrutura. Recursos AWS podem gerar custos: monitorar e excluir recursos quando não necessários.

**Bônus (até 10 pontos, respeitando teto definido pelo docente):** configurar domínio/TLS com justificativa, observabilidade adicional ou rollback automatizado seguro.
