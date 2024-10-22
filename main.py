import random

# Funções para geração de estratégias de ataque e defesa para os agentes da equipe

def gerar_estrategia_ataque(inimigos_visiveis, ponto_controle, equipe):
    estrategias = [
        "Flanquear inimigos",
        "Ataque direto",
        "Engajar de longa distância",
        "Capturar o ponto rapidamente"
    ]
    if inimigos_visiveis > 0:
        return f"Estratégia de ataque gerada para {equipe}: {random.choice(estrategias)} contra {inimigos_visiveis} inimigos no {ponto_controle}."
    else:
        return f"Estratégia de ataque gerada para {equipe}: Capturar {ponto_controle} sem resistência inimiga."

def gerar_estrategia_defesa(inimigos_proximos, ponto_defendido, equipe):
    estrategias_defesa = [
        "Montar barreira defensiva",
        "Fortificar ponto estratégico",
        "Colocar armadilhas",
        "Patrulhar área defensiva"
    ]
    if inimigos_proximos > 0:
        return f"Estratégia de defesa gerada para {equipe}: {random.choice(estrategias_defesa)} para defender {ponto_defendido} contra {inimigos_proximos} inimigos."
    else:
        return f"Estratégia de defesa gerada para {equipe}: Fortificar {ponto_defendido} sem resistência imediata."

def gerar_ordens_lider(ataque_resposta, defesa_resposta, equipe):
    estrategias_lider = [
        "Aumentar pressão no ataque",
        "Reforçar defesas",
        "Focar no controle de território",
        "Coordenar ataques de múltiplos flancos"
    ]
    return f"Ordens do Líder ({equipe}): {random.choice(estrategias_lider)}\n- {ataque_resposta}\n- {defesa_resposta}"

# Simulando situação de ataque e defesa para duas equipes (A e B)
inimigos_visiveis = 5
inimigos_proximos = 4
ponto_controle_A = "Ponto Alpha"
ponto_controle_B = "Ponto Beta"
ponto_defendido_A = "Base de Equipe A"
ponto_defendido_B = "Base de Equipe B"

# Chamando os agentes da Equipe A
ataque_resposta_A = gerar_estrategia_ataque(inimigos_visiveis, ponto_controle_A, "Equipe A")
defesa_resposta_A = gerar_estrategia_defesa(inimigos_proximos, ponto_defendido_A, "Equipe A")
coordenacao_lider_A = gerar_ordens_lider(ataque_resposta_A, defesa_resposta_A, "Equipe A")

# Chamando os agentes da Equipe B
ataque_resposta_B = gerar_estrategia_ataque(inimigos_visiveis, ponto_controle_B, "Equipe B")
defesa_resposta_B = gerar_estrategia_defesa(inimigos_proximos, ponto_defendido_B, "Equipe B")
coordenacao_lider_B = gerar_ordens_lider(ataque_resposta_B, defesa_resposta_B, "Equipe B")

# Exibindo a coordenação das duas equipes
print(f"Coordenação da Equipe A:\n{coordenacao_lider_A}\n")
print(f"Coordenação da Equipe B:\n{coordenacao_lider_B}\n")

# Salvando a saída em arquivos separados
output_path_A = 'interacao_agentes_fps_genai_equipe_A.txt'
output_path_B = 'interacao_agentes_fps_genai_equipe_B.txt'

with open(output_path_A, 'w') as f:
    f.write(coordenacao_lider_A)

with open(output_path_B, 'w') as f:
    f.write(coordenacao_lider_B)
