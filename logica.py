"""
BACKEND DO PROJETO – CRUD de Perguntas
Autor: Pessoa 1 (Lógica)
Responsabilidades:
- Manipular JSON
- Validar dados
- Fornecer funções para a interface
"""

import json
import os

ARQUIVO = "perguntas.json"


# ================================
#   1. CARREGAR DADOS
# ================================
def carregar_dados():
    """Lê o arquivo JSON e retorna uma lista de perguntas."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # arquivo corrompido → cria novo
    return []


# ================================
#   2. SALVAR DADOS
# ================================
def salvar_dados(perguntas):
    """Salva toda a lista de perguntas em JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(perguntas, f, indent=4, ensure_ascii=False)


# ================================
#   >>> VALIDAÇÃO DOS DADOS <<<
# ================================
def validar_pergunta(p):
    """
    Confere se a pergunta está completa.
    Deve conter:
    - pergunta (texto)
    - op1
    - op2
    - op3
    - correta  (0, 1 ou 2)
    """
    if not p.get("pergunta"):
        return False

    if not p.get("op1") or not p.get("op2") or not p.get("op3"):
        return False

    if p.get("correta") not in [0, 1, 2]:
        return False

    return True


# ================================
#   3. ADICIONAR
# ================================
def adicionar(perguntas, nova):
    """Adiciona nova pergunta ao JSON."""
    if not validar_pergunta(nova):
        raise ValueError("Dados incompletos ou incorretos.")

    perguntas.append(nova)
    salvar_dados(perguntas)
    print("Pergunta adicionada:", nova)

    return perguntas


# ================================
#   4. ATUALIZAR
# ================================
def atualizar(perguntas, indice, nova):
    """Atualiza pergunta existente."""
    if indice < 0 or indice >= len(perguntas):
        raise IndexError("Índice inválido.")

    if not validar_pergunta(nova):
        raise ValueError("Campos incompletos.")

    perguntas[indice] = nova
    salvar_dados(perguntas)
    print(f"Pergunta atualizada (índice {indice}):", nova)

    return perguntas


# ================================
#   5. EXCLUIR
# ================================
def excluir(perguntas, indice):
    """Remove uma pergunta pelo índice."""
    if indice < 0 or indice >= len(perguntas):
        raise IndexError("Índice inválido.")

    removida = perguntas.pop(indice)
    salvar_dados(perguntas)
    print(f"Pergunta removida:", removida)

    return perguntas



