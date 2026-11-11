def executar_quiz():
    # Lista de dicionarios contendo as perguntas, opcoes e a resposta correta
    perguntas = [
        {
            "pergunta": "O que e o Python?",
            "opcoes": [
                "A) Um sistema operacional",
                "B) Uma linguagem de programacao",
                "C) Um editor de codigo",
                "D) Um navegador web"
            ],
            "resposta": "b"
        },
        {
            "pergunta": "Qual palavra-chave e usada para definir uma funcao em Python?",
            "opcoes": [
                "A) func",
                "B) define",
                "C) def",
                "D) function"
            ],
            "resposta": "c"
        },
        {
            "pergunta": "Como se faz um comentario de uma unica linha em Python?",
            "opcoes": [
                "A) // Este e um comentario",
                "B) # Este e um comentario",
                "C) /* Este e um comentario */",
                "D) <!-- Este e um comentario -->"
            ],
            "resposta": "b"
        }
    ]

    pontuacao = 0

    print("=== BEM-VINDO AO QUIZ DE PROGRAMACAO ===")
    print("Responda com a letra correspondente (a, b, c ou d).\n")

    # Loop pelas perguntas usando enumerate para numerar cada questao
    for i, item in enumerate(perguntas, start=1):
        print(f"Questao {i}: {item['pergunta']}")
        for opcao in item['opcoes']:
            print(opcao)

        # Recebe a resposta do usuario, remove espacos e converte para minusculo
        resposta_usuario = input("Sua resposta: ").strip().lower()

        if resposta_usuario == item['resposta']:
            print("Correto!\n")
            pontuacao += 1
        else:
            print(f"Incorreto. A resposta correta era a opcao {item['resposta'].upper()}.\n")

    # Exibicao do resultado final
    print("=== FIM DO QUIZ ===")
    print(f"Voce acertou {pontuacao} de {len(perguntas)} questoes.")

    if pontuacao == len(perguntas):
        print("Parabens! Voce gabaritou o quiz.")
    elif pontuacao > 0:
        print("Bom trabalho! Continue praticando.")
    else:
        print("Nao desanime, estude mais um pouco e tente novamente.")

if __name__ == "__main__":
    executar_quiz()