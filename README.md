# Cloud Tasks API — Projeto Final de Computação em Nuvem

Aplicação Flask/SQLite preparada para um laboratório de **CI/CD com GitHub Actions, Docker, GHCR e AWS EC2**. A base contém código, testes e workflows; cabe ao grupo aprovisionar a nuvem, configurar segredos, usar branches/PRs, implementar uma evolução funcional e comprovar a esteira.

## Arquitetura
`Branch/PR -> CI (pytest + Docker build) -> merge main -> CI (publicação GHCR por SHA) -> CD (SSH EC2 + docker pull/run) -> /health`

## Rodar localmente
```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate  |  Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python -m pytest -q
python -m flask --app app.main run --port 5000
```
Ou execute `docker compose up --build` e abra `http://localhost:8080/health`.

## API
| Método | Rota | Função |
|---|---|---|
| GET | `/` | Informações |
| GET | `/health` | Saúde da aplicação/banco |
| GET | `/tasks` | Lista tarefas |
| POST | `/tasks` | Cria tarefa (`{"title":"..."}`) |
| PATCH | `/tasks/<id>` | Atualiza conclusão (`{"done":true}`) |

Exemplos:
```bash
curl http://localhost:8080/health
curl -X POST http://localhost:8080/tasks -H 'Content-Type: application/json' -d '{"title":"Minha tarefa"}'
curl http://localhost:8080/tasks
```

## Configuração AWS + GitHub
Leia [docs/CONFIGURACAO.md](docs/CONFIGURACAO.md).

## Seu desafio
1. Criar repositório próprio e configurar CI e CD reais na EC2.
2. Implementar `DELETE /tasks/<id>` (204 quando excluída, 404 caso contrário) e **dois testes automatizados** associados.
3. Adicionar **uma melhoria adicional**: filtro de tarefas por situação, rota `/version`, ou outra funcionalidade acordada com docente; incluir teste.
4. Demonstrar ao menos um PR com CI aprovado e um `push` na main que resulte em deploy, além de prova de persistência após reiniciar contêiner.
5. Preencher relatório com diagrama, decisões, evidências e custos/encerramento.

## Segurança e limitações didáticas
O deploy é simplificado: não há TLS, balanceamento, rollback automatizado nem alta disponibilidade. Não colocar dados reais na API e não usar este modelo sem endurecimento em produção. SSH a partir de runner hospedado exige planejamento de rede seguro; veja o guia. `docker` group equivale a privilégios elevados na EC2.
