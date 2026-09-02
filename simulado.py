import random
from time import sleep

banco_de_questoes = [
    {
        "pergunta": "O que são mudanças climáticas?",
        "opcao": ["A) Alterações apenas na temperatura durante o verão", "B) Alterações de longo prazo nos padrões do clima", "C) Mudanças que acontecem somente em cidades", "D) Alterações causadas apenas por fenômenos naturais"],
        "correta": "B"
        },
    {
        "pergunta": "Qual destes é um importante gás de efeito estufa?",
        "opcao": ["A) Oxigênio", "B) Nitrogênio", "C) Dióxido de carbono", "D) Hélio"],
        "correta": "C"
        },
    {
        "pergunta": "Qual atividade humana contribui bastante para o aumento das emissões de gases de efeito estufa?",
        "opcao": ["A) Queima de combustíveis fósseis", "B) Plantar árvores", "C) Reciclagem", "D) Uso de bicicleta"],
        "correta": "A"
        },
    {
        "pergunta": "Qual é uma consequência do aquecimento global?",
        "opcao": ["A) Diminuição da temperatura média da Terra", "B) Desaparecimento de todos os desertos", "C)Redução das ondas de calor", "D)Aumento do nível do mar"],
        "correta": "D"
        },
    {
        "pergunta": "O desmatamento pode contribuir para as mudanças climáticas porque:",
        "opcao": ["A)Pode liberar carbono armazenado na vegetação e no solo", "B)Aumenta a absorção de CO₂ pelas florestas", "C)Impede completamente as queimadas", "D)Diminui a quantidade de gases na atmosfera"],
        "correta": "A"
        },
    {
        "pergunta": "Por que os oceanos são importantes no sistema climático?",
        "opcao": ["A)Porque não sofrem alterações de temperatura", "B)Porque produzem todo o oxigênio da atmosfera", "C)Porque absorvem grande parte do calor extra do sistema climático", "D)Porque impedem qualquer mudança no clima"],
        "correta": "C"
        },
    {
        "pergunta": "O aumento de CO₂ na atmosfera também está relacionado a qual fenômeno?",
        "opcao": ["A)Acidificação dos oceanos", "B)Formação de neve nos desertos", "C)Redução da gravidade", "D)Diminuição dos ventos"],
        "correta": "A"
        },
    {
        "pergunta": "Qual destas atitudes pode ajudar a reduzir impactos ambientais?",
        "opcao": ["A)Desperdiçar água", "B)Aumentar o uso de produtos descartáveis", "C)Jogar lixo em rios", "D)Economizar energia e reduzir desperdícios"],
        "correta": "D"
        },
    {
        "pergunta": "Como as mudanças climáticas podem afetar os animais?",
        "opcao": ["A)Fazem todos os animais se adaptarem imediatamente", "B)Podem alterar habitats e disponibilidade de alimentos", "C)Não alteram os ecossistemas", "D)Afetam somente animais domésticos"],
        "correta": "B"
        },
    {
        "pergunta": "Qual afirmação está correta?",
        "opcao": ["A)O efeito estufa é totalmente ruim para a Terra", "B)O CO₂ não influencia o clima", "C)O efeito estufa natural ajuda a manter a Terra aquecida", "D)As atividades humanas não alteram o clima"],
        "correta": "C"
        },
]


async def rodar_simulado(ctx, bot):
    acertos = 0
    erros = 0
    questoes_do_teste = banco_de_questoes.copy()
    random.shuffle(questoes_do_teste)

    await ctx.send("=== INÍCIO DO SIMULADO ===")

    for numero, questao in enumerate(questoes_do_teste, 1):
        # Montando o texto da questão
        texto_questao = f"\n**Questão {numero}**\n"
        texto_questao += f"{questao['pergunta']}\n"
        for alternativa in questao["opcao"]:
            texto_questao += f"{alternativa}\n"
            
        await ctx.send(texto_questao)
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
          
        msg = await bot.wait_for('message', check=check)
        resposta = msg.content.strip().upper()
        
        if resposta == questao["correta"]:
            acertos += 1
            await ctx.send("✅ *Resposta correta!*")
        else:
            erros += 1
            await ctx.send(f"❌ *Resposta errada.* A alternativa correta era a **{questao['correta']}**")
            
        await ctx.send("----------------------------------------")
        
    await ctx.send("\n=== **FIM DO SIMULADO** ===")
    await ctx.send(f"🏆 Você acertou **{acertos}** questões e errou **{erros}**!!!")