
import discord
import random
import requests
import pyttsx3

from discord.ext import commands
from simulado import rodar_simulado

API_KEY = "SEU TOKEN"

PREFIXO = "#"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=PREFIXO,
    intents=intents
)


def speak(texto):
    engine = pyttsx3.init()

    engine.setProperty("rate", 180)

    engine.say(texto)
    engine.runAndWait()

    engine.stop()

lista_dicas = [
    "Reduza o consumo de produtos descartáveis e evite embalagens desnecessárias.",
    "Reutilize itens sempre que possível, como frascos e sacolas.",
    "Recicle materiais como papel, plástico e metal, separando corretamente o lixo.",
    "Economize água tomando banhos mais curtos e consertando vazamentos.",
    "Economize energia desligando aparelhos eletrônicos quando não estiverem em uso.",
    "Substitua lâmpadas incandescentes por LEDs.",
    "Opte por meios de transporte sustentáveis, como bicicleta e transporte público.",
    "Compre produtos orgânicos e locais sempre que possível, evitando alimentos processados e embalagens excessivas.",
    "Nunca jogue lixo no chão e sempre descarte corretamente os resíduos.",
    "Participe de mutirões de limpeza em sua comunidade.",
    "Plante árvores e cuide das áreas verdes ao seu redor."
]

lista_metas = [
    "Desafio da água: tome um banho mais curto hoje e evite deixar a torneira aberta sem necessidade.",
    "Desafio da energia: desligue as luzes de ambientes vazios e os aparelhos que não estiverem sendo usados.",
    "Desafio da reciclagem: separe corretamente os materiais recicláveis da sua casa.",
    "Desafio do lixo: passe um dia sem jogar nenhum lixo no chão.",
    "Desafio do descartável: evite usar copos, canudos ou talheres descartáveis quando puder usar reutilizáveis.",
    "Desafio do transporte: faça um trajeto curto caminhando ou de bicicleta em vez de usar carro.",
    "Desafio da natureza: cuide de uma planta ou árvore que esteja ao seu redor.",
    "Desafio das sacolas: use uma sacola reutilizável na próxima vez que fizer compras.",
    "Desafio contra o desperdício: coloque no prato apenas a quantidade de comida que você vai comer.",
    "Desafio do papel: evite imprimir algo que possa ser utilizado digitalmente.",
    "Desafio dos aparelhos: verifique se há aparelhos ligados sem necessidade e desligue os que puder.",
    "Desafio da reutilização: encontre um objeto que seria descartado e pense em uma forma de reutilizá-lo.",
    "Desafio de conscientização: conte para alguém uma coisa nova que você aprendeu sobre mudanças climáticas e explique por que ela é importante."
]

lista_curiosidades = [
    "A Terra já aqueceu cerca de 1,1 °C desde o período de 1850–1900, principalmente por causa das atividades humanas.",
    "O nível médio do mar está subindo porque o oceano se expande quando aquece e porque o gelo que está sobre a terra derrete.",
    "O efeito estufa natural é essencial para a vida. O problema é o aumento da concentração de gases de efeito estufa causado principalmente pelas atividades humanas.",
    "O aumento de CO₂ também contribui para a acidificação dos oceanos, alterando a química da água do mar.",
    "O aquecimento dos oceanos pode afetar os animais marinhos, porque mudanças de temperatura alteram habitats e condições de vida.",
    "Geleiras e mantos de gelo estão diminuindo, sendo uma das evidências observadas das mudanças climáticas.",
    "As mudanças climáticas podem alterar onde plantas e animais conseguem viver, fazendo algumas espécies mudarem sua distribuição geográfica.",
    "Em algumas regiões, plantas estão florescendo mais cedo do que acontecia no passado, uma mudança associada ao aquecimento do clima.",
    "Satélites são usados para acompanhar mudanças no nível dos oceanos, permitindo medir alterações em escala global.",
    "Mudança climática e aquecimento global não são exatamente a mesma coisa. Aquecimento global é o aumento de longo prazo da temperatura média, enquanto mudança climática envolve alterações mais amplas no sistema climático.",
    "As mudanças climáticas podem influenciar eventos extremos, incluindo ondas de calor, secas, chuvas intensas e incêndios em determinadas regiões.",
    "A principal causa do aquecimento global atual é humana, especialmente a emissão de gases de efeito estufa pela queima de combustíveis fósseis."
]



@bot.event
async def on_ready():
    print(f"✅ Estamos entrando como {bot.user}")

@bot.command()
async def ola(ctx):
    await ctx.send(
        f"Olá {ctx.author.mention} 💚💚💚")

@bot.command()
async def mudancas_climaticas(ctx):
    await ctx.send(
        f"{ctx.author.mention}, mudanças climáticas são alterações de longo prazo "
        "nos padrões do clima da Terra, como a temperatura 🌡️.\n\n"

        "Os gases de efeito estufa são importantes para manter a Terra aquecida 🔥, "
        "mas as atividades humanas aumentam a concentração desses gases, "
        "contribuindo para o aquecimento global.\n\n"

        "⚠️ **PRINCIPAIS CAUSAS:**\n"
        "• Queima de combustíveis fósseis, como carvão e petróleo 🔥\n"
        "• Desmatamento e queimadas 🌳\n"
        "• Atividades industriais e produção de energia ⚡\n\n"

        "🌎 **PRINCIPAIS CONSEQUÊNCIAS:**\n"
        "• Aumento da temperatura média da Terra\n"
        "• Elevação do nível do mar\n"
        "• Derretimento de geleiras\n"
        "• Ondas de calor intensas\n"
        "• Secas prolongadas\n"
        "• Alterações nos ecossistemas"
    )

@bot.command()
async def lixo(ctx):
    await ctx.send(
        f"{ctx.author.mention}, as cores dos lixos são 🗑️:\n\n"
        "🟦 Azul - Papel e papelão\n"
        "🟩 Verde - Vidro\n"
        "🟥 Vermelho - Plástico\n"
        "🟨 Amarelo - Metal\n"
        "🟫 Marrom - Resíduos orgânicos"
    )

@bot.command()
async def dica(ctx):

    dica_aleatoria = random.choice(lista_dicas)
    titulo = "DICA AMBIENTAL"
    embed = discord.Embed(title=f"🌱 {titulo}:",description=dica_aleatoria,color=0x2ECC71)

    await ctx.send(embed=embed)
    speak(f"{titulo}. {dica_aleatoria}")


@bot.command()
async def meta(ctx):

    meta_aleatoria = random.choice(lista_metas)
    titulo = "META AMBIENTAL"
    embed = discord.Embed(title= f"🎯 {titulo}:",description=meta_aleatoria,color=0x2ECC71)

    await ctx.send(embed=embed)
    speak(f"{titulo}. {meta_aleatoria}")


@bot.command()
async def curiosidade(ctx):

    curiosidade_aleatoria = random.choice(lista_curiosidades)
    titulo = "VOCÊ SABIA?"
    embed = discord.Embed(title= f"💡 {titulo}",description=curiosidade_aleatoria,color=0x2ECC71)

    await ctx.send(embed=embed)
    speak(f'{titulo}. {curiosidade_aleatoria}')


@bot.command()
async def fauna(ctx):

    await ctx.send(
        f"{ctx.author.mention}, alguns animais que podem ser prejudicados "
        "pelas mudanças climáticas são:\n\n"

        "🐻‍❄️ **Ursos-polares** - devido à redução do gelo marinho.\n"
        "🐘 **Elefantes** - devido à perda de habitat causada por mudanças ambientais.\n"
        "🐳 **Baleias** - devido às alterações na temperatura dos oceanos.\n"
        "🐝 **Abelhas** - devido às mudanças nos habitats e na disponibilidade de plantas.\n\n"

        "🌎 Existem muitos outros animais afetados pelas mudanças climáticas."
    )

@bot.command()
async def quiz(ctx):
    await rodar_simulado(ctx, bot)

@bot.command()
async def clima(ctx, *, cidade):

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": cidade,
        "lang": "pt"
    }

    resposta = requests.get(url, params=params)

    if resposta.status_code != 200:
        await ctx.send(
            "❌ Não consegui encontrar essa cidade."
        )
        return

    dados = resposta.json()

    temperatura = dados["current"]["temp_c"]
    sensacao = dados["current"]["feelslike_c"]
    umidade = dados["current"]["humidity"]
    condicao = dados["current"]["condition"]["text"]

    await ctx.send(
        f"🌎 **Clima em {cidade}**\n\n"
        f"🌡️ Temperatura: **{temperatura}°C**\n"
        f"🤔 Sensação: **{sensacao}°C**\n"
        f"💧 Umidade: **{umidade}%**\n"
        f"☁️ Condição: **{condicao}**"
    )
    speak(
        f'Clima em {cidade}.'
        f'Temperatura de {temperatura} graus Celsius. '
        f'Sensação térmica de {sensacao} graus Celsius. '
        f'Umidade de {umidade} por cento. '
        f'Condição: {condicao}. '
    )


@bot.command()
async def ajuda(ctx):

    await ctx.send(
        f"{ctx.author.mention}, meus comandos são:\n\n"

        "👋 **#ola** - Me apresento ao usuário\n"
        "🌎 **#mudancas_climaticas** - Explico sobre mudanças climáticas, "
        "suas causas e consequências\n"
        "🗑️ **#lixo** - Mostro as cores dos tipos de resíduos\n"
        "🌱 **#dica** - Dou uma dica ambiental aleatória e falo a dica\n"
        "🎯 **#meta** - Defino uma meta ambiental\n"
        "💡 **#curiosidade** - Mando uma curiosidade sobre mudanças climáticas\n"
        "🐾 **#fauna** - Mostro animais afetados pelas mudanças climáticas\n"
        "🧠 **#quiz** - Faço um quiz sobre mudanças climáticas\n"
        "🌤️ **#clima [cidade]** - Mostro o clima atual de uma cidade\n"
        "📚 **#ajuda** - Mostro esta lista de comandos"
    )

bot.run("SEU TOKEN")